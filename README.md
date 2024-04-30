
(Note: The bash version might be inhibited because the config files were slightly modified)

# Bash version

Use the `case_init.sh`.

Do not change the function. Simply adjust your settings in the lower part of the code. Lastly, execute the script `bash case_init.sh`.

# Python version (new)

Use the `user_data.py` and `run_CLM5_case.py`.

Create your dictionary with the proper CLM5 case settings in the `user_data.py`. The CLM5 case is a python dataclass, and you can see and add adjustable settings in the `CLM5_data.py` file under the `case` class.
You can then turn off / on the steps you want the script to do in the `run_CLM5_case.py` by e.g. commenting out respective lines.

When done, simply execute `python run_CLM5_case.py`.

Corrections, comments, suggestions are welcome.

# CLM5EU3_GPP-ET_GMD_paper
The corresponding configurations are in `cases_CLM5EU3_split.py`. Please refer to the `CLM5.py` base class for adjustments and for running the case `run_CLM5_case_split.py`.
