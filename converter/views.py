from django.views.generic import TemplateView
from django.http import JsonResponse

class BaseConversionView(TemplateView):
    """
    Base view for unit conversions. Provides shared functionality for all types of conversions.
    """
    template_name = None  # Must be overridden in subclass

    def get_context_data(self, **kwargs):
        """
        Prepare the context with default values and options.
        """
        context = super().get_context_data(**kwargs)
        context['converted_value'] = None
        context['error'] = None
        context['units'] = self.get_units()  # Fetch units from subclass
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle form submissions.
        """
        value = request.POST.get('value')
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        try:
            value = float(value)
            converted_value = self.convert_value(value, from_unit, to_unit)
            context = self.get_context_data()
            context['converted_value'] = f"{value} {from_unit} = {converted_value} {to_unit}"
        except (ValueError, TypeError) as e:
            context = self.get_context_data()
            context['error'] = "Invalid input. Please enter a valid number and select units."
        except Exception as e:
            context = self.get_context_data()
            context['error'] = str(e)

        return self.render_to_response(context)

    def get_units(self):
        """
        Define available units for conversion. Must be overridden in subclass.
        """
        raise NotImplementedError("Subclasses must implement `get_units` method.")

    def convert_value(self, value, from_unit, to_unit):
        """
        Perform the conversion. Must be overridden in subclass.
        """
        raise NotImplementedError("Subclasses must implement `convert_value` method.")







from .utils import convert_length

class LengthConversionView(BaseConversionView):
    template_name = 'converter/length.html'

    def get_units(self):
        return ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']

    def convert_value(self, value, from_unit, to_unit):
        return convert_length(value, from_unit, to_unit)








from .utils import convert_weight

class WeightConversionView(BaseConversionView):
    template_name = 'converter/weight.html'

    def get_units(self):
        return ['milligram', 'gram', 'kilogram', 'ounce', 'pound']

    def convert_value(self, value, from_unit, to_unit):
        return convert_weight(value, from_unit, to_unit)








from .utils import convert_temperature

class TemperatureConversionView(BaseConversionView):
    template_name = 'converter/temperature.html'

    def get_units(self):
        return ['Celsius', 'Fahrenheit', 'Kelvin']

    def convert_value(self, value, from_unit, to_unit):
        return convert_temperature(value, from_unit, to_unit)
