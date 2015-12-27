from .base import VarAtts
from ..data import time
import numpy as np

nan = np.float32(np.NaN)


# Currently all of the 'meta' variables are commented out.
# This could be changed after meta-arrays are implemented.

vec_data = {
    'AnaIn2LSB': VarAtts(dims=[],
                         dtype=np.uint8,
                         group='_extra',
                         ),
    'Count': VarAtts(dims=[],
                     dtype=np.uint8,
                     group='_extra',
                     ),
    'PressureMSB': VarAtts(dims=[],
                           dtype=np.uint8,
                           group='env',
                           ),
    'AnaIn2MSB': VarAtts(dims=[],
                         dtype=np.uint8,
                         group='_extra',
                         ),
    'PressureLSW': VarAtts(dims=[],
                           dtype=np.uint16,
                           group='env',
                           ),
    'AnaIn1': VarAtts(dims=[],
                      dtype=np.uint16,
                      group='_extra',
                      ),
    'vel': VarAtts(dims=[3],
                   dtype=np.float32,
                   group=None,
                   factor=0.001,
                   default_val=nan,
                   ),
    'amp': VarAtts(dims=[3],
                   dtype=np.uint8,
                   group='sys',
                   # title_name='Amp',
                   # units='Counts',
                   # dim_names=['xyz'],
                   ),
    'corr': VarAtts(dims=[3],
                    dtype=np.uint8,
                    group='sys',
                    # title_name='Corr',
                    # units='%',
                    # dim_names=['xyz', 'time'],
                    ),
}

vec_sysdata = {
    'mpltime': VarAtts(dims=[],
                       dtype=np.float64,
                       group=None,
                       view_type=time.time_array,
                       default_val=nan,
                       ),
    'batt': VarAtts(dims=[],
                    dtype=np.float32,
                    group='sys',
                    default_val=nan,
                    factor=0.1,
                    # units={'V': 1},
                    # dim_names=['time'],
                    # title_name='Batt',
                    ),
    'c_sound': VarAtts(dims=[],
                       dtype=np.float32,
                       group='env',
                       default_val=nan,
                       factor=0.1,
                       # title_name='c',
                       # dim_names=['time'],
                       # units={'m': 1, 's': -1},
                       ),
    'heading': VarAtts(dims=[],
                       dtype=np.float32,
                       group='orient',
                       default_val=nan,
                       factor=0.1,
                       # title_name='heading',
                       # units={'deg_true': 1},
                       # dim_names=['time'],
                       ),
    'pitch': VarAtts(dims=[],
                     dtype=np.float32,
                     group='orient',
                     default_val=nan,
                     factor=0.1,
                     # title_name='pitch',
                     # units={'deg': 1},
                     # dim_names=['time'],
                     ),
    'roll': VarAtts(dims=[],
                    dtype=np.float32,
                    group='orient',
                    default_val=nan,
                    factor=0.1,
                    # title_name='roll',
                    # units={'deg': 1},
                    # dim_names=['time'],
                    ),
    'temp': VarAtts(dims=[],
                    dtype=np.float32,
                    group='env',
                    default_val=nan,
                    factor=0.01,
                    # title_name='T',
                    # units={'C':1},
                    # dim_names=['time'],
                    ),
    'error': VarAtts(dims=[],
                     dtype=np.uint8,
                     group='sys',
                     default_val=nan,
                     ),
    'status': VarAtts(dims=[],
                      dtype=np.uint8,
                      group='sys',
                      default_val=nan,
                      ),
    'AnaIn': VarAtts(dims=[],
                     dtype=np.float32,
                     group='_extra',
                     default_val=nan,
                     ),
}

awac_profile = {
    'mpltime': VarAtts(dims=[],
                       dtype=np.float64,
                       view_type=time.time_array,
                       group=None,
                       # dim_names=['time'],
                       ),
    'Error': VarAtts(dims=[],
                     dtype=np.uint16,
                     group='sys',
                     # dim_names=['time'],
                     ),
    'AnaIn1': VarAtts(dims=[],
                      dtype=np.float32,
                      group='_extra',
                      default_val=nan,
                      # dim_names=['time'],
                      ),
    'batt': VarAtts(dims=[],
                    dtype=np.float32,
                    group='sys',
                    default_val=nan,
                    factor=0.1,
                    # title_name='batt',
                    # units={'V': 1}
                    # dim_names=['time'],
                    ),
    'c_sound': VarAtts(dims=[],
                       dtype=np.float32,
                       group='env',
                       default_val=nan,
                       factor=0.1,
                       # dim_names=['time'],
                       # title_name='c',
                       # units={'m': 1, 's': -1},
                       ),
    'heading': VarAtts(dims=[],
                       dtype=np.float32,
                       group='orient',
                       default_val=nan,
                       factor=0.1,
                       # dim_names=['time'],
                       # units={'deg_true': 1},
                       # title_name='heading',
                       ),
    'pitch': VarAtts(dims=[],
                     dtype=np.float32,
                     group='orient',
                     default_val=nan,
                     factor=0.1,
                     # dim_names=['time'],
                     # units={'deg': 1},
                     # title_name='pitch',
                     ),
    'roll': VarAtts(dims=[],
                    dtype=np.float32,
                    group='orient',
                    default_val=nan,
                    factor=0.1,
                    # dim_names=['time'],
                    # units={'deg': 1},
                    # title_name='roll',
                    ),
    'pressure': VarAtts(dims=[],
                        dtype=np.float32,
                        group='env',
                        default_val=nan,
                        factor=0.001,
                        # units={'dbar': 1},
                        # dim_names=['time'],
                        # title_name='P',
                        ),
    'status': VarAtts(dims=[],
                      dtype=np.float32,
                      group='sys',
                      default_val=nan,
                      ),
    'temp': VarAtts(dims=[],
                    dtype=np.float32,
                    group='env',
                    default_val=nan,
                    ),
    'vel': VarAtts(dims=[3, 'nbins', 'n'],
                   dtype=np.float32,
                   group=None,
                   default_val=nan,
                   factor=0.001,
                   # title_name='u',
                   # dim_names=['xyz', 'depth', 'time', ],
                   # units={'m': 1, 's': -1},
                   ),
    'amp': VarAtts(dims=[3, 'nbins', 'n'],
                   dtype=np.uint8,
                   group='sys',
                   # dim_names=['time', 'depth', 'time',],
                   ),
}
