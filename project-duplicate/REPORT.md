When installing the necessary libraries, needed to install an older version of python; installed the version 3.9.9.

When executing the training, found the problem "[WinError 1455] The paging file is too small for this operation to complete"; solved it by lowering the number of jobs for the trainnig.

The previous problem occurred again when training the scale factor 2, but I suppose it was because I incressed the number of jobs beforehand to test if it would run, to solve it I just runned again with decreassed number of jobs.

