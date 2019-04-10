import unittest
import time

"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

sleep_duration = 0


def job_scheduler(job, n):
    """
    Invokes the input function after n milliseconds

    :param job: The desired function to be invoked
    :param n: The duration in milliseconds after which :param job is invoked
    :return float: USED FOR TESTING. RETURNS THE TIME TOOK BEFORE CALLING AND AFTER CALLING THE FUNCTION
    """

    # Edge cases -->
    if not callable(job):
        raise TypeError("{} is not callable. The parameter job requires a function", type(job))

    if n is None:
        raise TypeError("n should be provided. Provided none")

    if n < 0:
        raise ValueError("n should be positive")
    # <-- Edge cases

    global sleep_duration  # To keep track of runtime

    start_time = time.time()
    time.sleep(n / 1000)  # Sleep for n milliseconds before invoking function
    end_time = time.time()

    sleep_duration = end_time - start_time  # Calculate sleep duration
    job()  # Invoke the function
    return sleep_duration * 1000  # Return the sleep duration in milliseconds


class Test(unittest.TestCase):
    """
    Using tolerance in the test cases, since time.sleep(1000) doesn't really sleep for 1000 milliseconds.
    It sleeps for "almost" 1000 milliseconds
    """

    def setUp(self):
        def job():
            return "This is the job"

        self.job = job

    def test_base_case(self):
        n = 1000
        tolerance = 10
        self.assertTrue(n - tolerance <= job_scheduler(self.job, n) <= n + tolerance)

    def test_case_2_seconds(self):
        n = 2000
        tolerance = 10
        self.assertTrue(n - tolerance <= job_scheduler(self.job, n) <= n + tolerance)

    def test_job_none(self):
        self.assertRaises(TypeError, job_scheduler, None, 1)

    def test_job_none_and_negative_time(self):
        self.assertRaises(TypeError, job_scheduler, self.job, None)
        self.assertRaises(ValueError, job_scheduler, self.job, -1)


if __name__ == '__main__':
    unittest.main()
