# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import pyqrcode 
import png 
from pyqrcode import QRCode 
from odoo.exceptions import Warning

  
class UploadMenu(models.Model):
    _name = 'upload.menu'
    _rec_name = 'hotel_name'

    _sql_constraints = [ ('hotel_number','UNIQUE (hotel_number)','Hotel Menu all already exists')]

    hotel_name = fields.Char('Hotel Name')
    hotel_menu = fields.Binary('Hotel Menu')
    hotel_number = fields.Char("Hotel Number")
    filename = fields.Char()

    @api.model
    def create(self, vals):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
       	url = pyqrcode.create('http://71b94cef4d5e.ngrok.io' + '/' + vals.get('hotel_name') + '/' + vals.get('hotel_number'))
       	url.png('/home/serpentcs/workspace/project/projects_v12/digital_menu/static/menus/%s' %(vals.get('hotel_name')), scale = 6) 
        self._compute_access_url(vals)
        return super(UploadMenu, self).create(vals)
	    
    @api.multi
    def _compute_access_url(self, vals):
        self.access_url = '/%s/%s' % (vals.get('hotel_name'), vals.get('hotel_number'))