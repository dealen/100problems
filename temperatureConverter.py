__author__ = 'dealen'

class ConvertTemperatures:
    base_measurement = ''
    output_measurement = ''
    value_for_conversion = 0.0
    output_measurement_full = ''

    def convert(self, value, base, output):
        self.value_for_conversion = value
        self.base_measurement = base
        self.output_measurement = output

        if self.output_measurement == 'C':
            self.output_measurement_full = 'Celsius'
        elif self.output_measurement == 'F':
            self.output_measurement_full = 'Fahrenheit'
        elif self.output_measurement == 'K':
            self.output_measurement_full = 'Kelvin'

        if self.base_measurement == self.output_measurement:
            print('Error, base and output measurement are the same, please choose different.')
        else:
            if self.base_measurement == 'C':
                print('Result from conversion Celsius -> ', self.output_measurement_full, ' = ',
                      str(self.convert_from_celsius()))
            elif self.base_measurement == 'F':
                print('Result from conversion Fahrenheit -> ', self.output_measurement_full, ' = ',
                      str(self.convert_from_fahrenheit()))
            elif self.base_measurement == 'K':
                print('Result from conversion Kelvin -> ', self.output_measurement_full, ' =  ',
                      str(self.convert_from_kelvin()))
            else:
                print('Please, enter proper base measurement.')

    def convert_from_celsius(self):
        if self.output_measurement == 'F':
            return self.value_for_conversion * 9.0 / 5.0 + 32.0
        elif self.output_measurement == 'K':
            return self.value_for_conversion + 273.15

    def convert_from_fahrenheit(self):
        if self.output_measurement == 'C':
            return (self.value_for_conversion - 32.0) * 5.0 / 9.0
        elif self.output_measurement == 'K':
            return (self.value_for_conversion + 459.67) * 5.0 / 9.0

    def convert_from_kelvin(self):
        if self.output_measurement == 'C':
            return self.value_for_conversion - 273.15
        elif self.output_measurement == 'F':
            return self.value_for_conversion * 9.0 / 5.0 - 459.67


value_for_conversion = float(input('Enter value for conversion :'))

while value_for_conversion != -1:
    which_measurement_base = input('Enter base measurement (C for Celsius, K for Kelvin or F for Fahrenheit :')
    which_measurement_output = input('Enter output measurement (C for Celsius, K for Kelvin or F for Fahrenheit :')
    converter = ConvertTemperatures()
    converter.convert(value_for_conversion, which_measurement_base, which_measurement_output)
    value_for_conversion = float(input('If you want to convert another value, please enter it.'
                                 'If not, enter -1.'))
