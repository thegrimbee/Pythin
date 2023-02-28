try:
    from pythin_class import Pythin
    from level0_submission_solution import clear_yard as solve_submission_level0
    from level0_real_solution import clear_yard as solve_real_level0
    from level1_submission_solution import clear_yard as solve_submission_level1
    from level1_real_solution import clear_yard as solve_real_level1
except:
    from solutions.pythin_class import Pythin
    from solutions.level0_submission_solution import clear_yard as solve_submission_level0
    from solutions.level0_real_solution import clear_yard as solve_real_level0
    from solutions.level1_submission_solution import clear_yard as solve_submission_level1
    from solutions.level1_real_solution import clear_yard as solve_real_level1



def solve(items, level_number):
    submission_pythin = Pythin(items)
    real_pythin = Pythin(items)
    if level_number == 0:
        try:
            solve_submission_level0(submission_pythin)
        except Exception as error:
            submission_pythin.status = error
        solve_real_level0(real_pythin)
    elif level_number == 1:
        try:
            solve_submission_level1(submission_pythin)
        except Exception as error:
            submission_pythin.status = error
        solve_real_level1(real_pythin)
    return submission_pythin.moves, submission_pythin.swallow_count, real_pythin.swallow_count, submission_pythin.status


solve(["rat", "rat", "rat"], 1)