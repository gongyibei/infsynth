from ..signal import analog_warpper
from numpy import tan, cos, pi
from scipy.signal import lfilter

@analog_warpper
def lpf(A, nf):
    """
    First-order low-pass filter

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    b = [tan(wc/2), tan(wc/2)]
    a = [1+tan(wc/2), -(1-tan(wc/2))]
    return lambda t: lfilter(b, a, A(t))

@analog_warpper
def hpf(A, nf):
    """
    First-order high-pass filter

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    b = [1, -1]
    a = [1 + tan(wc/2), -(1-tan(wc/2))]
    return lambda t: lfilter(b, a, A(t))

    
@analog_warpper
def lsf(A, nf, G):
    """
    First-order low-shelf filter

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_
    G : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    b = [1 + G*tan(wc/2), -(1-G*tan(wc/2))]
    a = [1 + tan(wc/2), -(1-tan(wc/2))]
    return lambda t: lfilter(b, a, A(t))

    
@analog_warpper
def hsf(A, nf, G):
    """
    First-order high-shelf filter

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_
    G : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    b = [tan(wc/2) + G, tan(wc/2) - G]
    a = [1 + tan(wc/2), -(1-tan(wc/2))]
    return lambda t: lfilter(b, a, A(t))

@analog_warpper
def bpf(A, nf, bw):
    """
    Second-order band-pass filter

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_
    bw : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    B = 2 * pi * bw
    b = [tan(B/2), 0, -tan(B/2)]
    a = [1 + tan(B/2), -2 * cos(wc), 1 - tan(B/2)]
    return lambda t: lfilter(b, a, A(t))


@analog_warpper
def bsf(A, nf, bw):
    """
    Second-order band-stop filter 

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_
    bw : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    B = 2 * pi * bw
    b = [1, -2 * cos(wc), 1]
    a = [1 + tan(B/2), -2 * cos(wc), 1 - tan(B/2)]
    return lambda t: lfilter(b, a , A(t))

@analog_warpper
def pnf(A, nf, bw, G):
    """
    Peaking or notch filter
    

    Parameters
    ----------
    A : _type_
        _description_
    nf : _type_
        _description_
    bw : _type_
        _description_
    G : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """    
    wc = 2 * pi * nf
    B = 2 * pi * bw
    b = [1 + G * tan(B/2), -2 * cos(wc), 1 - G*tan(B/2)]
    a = [1 + tan(B/2), -2 * cos(wc), 1 - tan(B/2)]
    return lambda t: lfilter(b, a , A(t))