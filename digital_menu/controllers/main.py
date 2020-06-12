# See LICENSE file for full copyright and licensing details.

import odoo
import base64
from odoo import http
from odoo.http import request



class UploadMenuController(http.Controller):

    @http.route(['/<string:hotel_name>/<string:hotel_number>'],
                type='http',
                auth='public',
                csrf=True)
    def _get_upload_menu(self, **kw):
            hotel_details = request.env['upload.menu'].sudo().search(
                [('hotel_name', '=', kw.get('hotel_name')),('hotel_number', '=', kw.get('hotel_number'))])
            for image in hotel_details:
                if (image.filename).split(".")[-1] in ['pdf', 'PDF']:
                    # file1 = open("/home/serpentcs/workspace/project/projects_v12/digital_menu/static/menus/myfile.txt","w") 
                    # file1.write((image.hotel_menu).decode('utf-8'))
                    #pdf file show
                    pdf_tag = '<iframe src="data:application/pdf;base64,{0}" target="_blank" type="application/pdf" height="100%" width="100%">'.format(
                        (image.hotel_menu).decode('utf-8'))
                    return pdf_tag
                else:
                    #img file show
                    img_tag = '<img src="data:image/png;base64,{0}" width="100%" height="100%">'.format(
                        (image.hotel_menu).decode('utf-8'))
                    return img_tag

        
        