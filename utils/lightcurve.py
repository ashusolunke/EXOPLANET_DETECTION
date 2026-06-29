import numpy as np
from scipy.optimize import curve_fit

def transit_model(time, t0, depth, duration, baseline):
    """
    A simple simplified Box-least-squares (BLS) style transit model.
    It returns a U-shaped or box-shaped dip in flux.
    """
    flux = np.ones_like(time) * baseline
    
    # Identify points inside the transit duration
    # We use a smooth approximation to avoid strict step functions which confuse curve_fit
    # but a simple box is also fine if initial guesses are good.
    
    half_dur = duration / 2.0
    
    # Boolean mask for the box
    in_transit = np.abs(time - t0) < half_dur
    flux[in_transit] -= depth
    
    # Adding a small sloping edge (limb darkening approximation) can help optimization
    # but for hackathon demonstration, a simple box is acceptable.
    
    return flux

def smooth_transit_model(time, t0, depth, duration, baseline):
    """
    A smoother approximation of a transit using a hyper-Gaussian 
    to allow gradient-based optimizers to find the minimum more reliably.
    """
    # Exponent determines sharpness of the box (e.g. 10 is very boxy)
    p = 10.0 
    dip = depth * np.exp(-0.5 * (np.abs(time - t0) / (duration / 2.0))**p)
    return baseline - dip

def fit_lightcurve(time, flux):
    """
    Fits the smooth transit model to the noisy light curve data.
    Returns the estimated parameters and the fitted model curve.
    """
    # Provide sensible initial guesses based on data
    # t0 guess: time of minimum flux
    t0_guess = time[np.argmin(flux)]
    # baseline guess: median flux
    baseline_guess = np.median(flux)
    # depth guess: baseline - min flux
    depth_guess = baseline_guess - np.min(flux)
    # duration guess: arbitrarily 0.5 for stability
    duration_guess = 0.5 
    
    initial_guess = [t0_guess, depth_guess, duration_guess, baseline_guess]
    
    # Bounds to prevent unphysical values
    # t0: within time array
    # depth: between 0 and 1
    # duration: > 0.01
    # baseline: around 1.0
    bounds = (
        [time[0], 0.0, 0.01, 0.9],
        [time[-1], 1.0, np.ptp(time), 1.1]
    )
    
    try:
        popt, pcov = curve_fit(
            smooth_transit_model, 
            time, 
            flux, 
            p0=initial_guess, 
            bounds=bounds,
            maxfev=10000
        )
        
        # Calculate fitted curve
        fitted_flux = smooth_transit_model(time, *popt)
        
        return {
            "success": True,
            "t0": popt[0],
            "depth": popt[1],
            "duration": popt[2],
            "baseline": popt[3],
            "fitted_flux": fitted_flux
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def calculate_snr(flux, fitted_flux, depth):
    """
    Calculates the Signal-to-Noise Ratio (SNR).
    SNR = depth / standard_deviation(out_of_transit_noise)
    """
    # Calculate residuals
    residuals = flux - fitted_flux
    # Noise standard deviation
    noise_std = np.std(residuals)
    
    if noise_std == 0:
        return 0
        
    return float(depth / noise_std)
