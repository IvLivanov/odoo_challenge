from odoo import api, fields, models, tools
import openai
import os



class Request(models.Model):
    #This class describes a quote request object:

    _name = 'request.request'
    _description = 'quote request'

    client = fields.Char(string='Client', required=True)
    product= fields.Char(string='Product', required=True)
    supplier= fields.Char(string='Supplier', required=True)
    #quote_request is defined, but not accessible. It will be generated with openai
    quote_request = fields.Text(string='Quote Request', readonly=True, store=True)

    #Decorator of object creation: it queries openai to create text for quote request
    @api.model
    def create(self, values):
        # Generate the quote request
          openai.api_key = os.environ.get('OPENAI_API_KEY')
          client = values['client']
          supplier = values['supplier']
          product = values['product']
          prompt = f"""I work in a Spear project. I need to request a quote on behalf of my customer, {client}. 
          They want to purchase {product} from {supplier}.
          Could you generate an email politely requesting a quote on behalf of {client}?
          Please, answer only the quote request and nothing else. Do not include generic fields like [Your Name]:
          If you are not sure - make your best guess. E.g. dear {supplier} team.
          you must not include any fields in []: the quote must be ready to send.
          use Spear Team instead of my name in the end """
          try:
            values['quote_request'] = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
            )["choices"][0]["message"]["content"]
          except:
            #This code just demonstrates  the possibility of openai failure.
            #In current prototype, quote just recives a special value.
            #For real applications, this event shall be handled properly. 
            values['quote_request']='DO NOT SEND THIS QUOTE: connection to chatGPT failed'
          return super(Request, self).create(values)