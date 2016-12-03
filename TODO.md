General
=======

Support for 3-beam solutions in rotations for adp's (i.e. in adp.rotate.beam2inst)

ADV burst mode: need to add checks that turbulence averaging doesn't "cross bursts"".

What if I want 30-minute turbulence averages spaced 15-minutes apart?
  - add `n_pad` option to `TurbBinner.__init__`, or
  - Add capability for `n_fft` > `n_bin`?

What about dropping data from averaging? Is this something we should support? Via negative `n_pad`?!?

Add updated Nortek ``.dep`` files, and document the Vector SW version somewhere.

Move ``api`` files to ``__init__`` files (and document this!)

Testing
======

Add tests to confirm that all scripts work.

Add tests to confirm that matlab file I/O works.

Documentation
====

Add some examples to the plotting tools page

Add usage examples for the adp package.