import unittest
import sensor_validate


class SensorValidatorTest(unittest.TestCase):
    def test_reports_error_when_soc_jumps(self):
        self.assertFalse(
            sensor_validate.is_sensor_reading_proper([0.0, 0.01, 0.5, 0.51], 'soc')
        )
        self.assertTrue(
            sensor_validate.is_sensor_reading_proper([0.0, 0.01, None, 0.02, 0.03], 'soc')
        )

    def test_reports_error_when_current_jumps(self):
        self.assertFalse(
            sensor_validate.is_sensor_reading_proper([0.03, 0.03, 0.03, 0.33], 'current')
        )
        self.assertTrue(
            sensor_validate.is_sensor_reading_proper([0.03, 0.03, 0.03, 0.04,None, None], 'current')
        )


if __name__ == "__main__":
    unittest.main()
