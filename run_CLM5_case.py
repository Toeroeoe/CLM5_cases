import user_data
import CLM5_data


# Settings
name_case           = 'CLM5_BGC_EUR_0275_ML_east_0000'
do_setup_clean      = False
do_build_clean      = False


# Main
my_case = CLM5_data.case(**getattr(user_data, name_case))

my_case.create()
my_case.setup(clean = do_setup_clean)
my_case.config()
my_case.namelists()
my_case.streams()
my_case.build(clean = do_build_clean)
my_case.submit()
