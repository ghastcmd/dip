When installing the necessary libraries, needed to install an older version of python; installed the version 3.9.9.

When executing the training, found the problem "[WinError 1455] The paging file is too small for this operation to complete"; solved it by lowering the number of jobs for the trainnig.

The previous problem occurred again when training the scale factor 2, but I suppose it was because I incressed the number of jobs beforehand to test if it would run, to solve it I just runned again with decreassed number of jobs.

Occurred another issue when trying to execute the test of the scripts. The message that appreared was "[Errno 2] No such file or directory: '_bicubic_x2.\\test\\butterfly_GT_bicubic_x3_bicubic_x2.bmp'". It was caused by a dot '.' withing the path to the image file.