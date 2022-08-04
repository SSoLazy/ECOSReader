import sys
from open_ecos_reader import ECOSReader

__version__ = '0.1.0'
__all__ = ['__version__', 'ECOSReader']

sys.modules['OpenECOSReader'] = ECOSReader