from openerp.osv import osv, fields as fields7
from openerp import models,fields, api

# class Purchase(osv.osv):
class Purchase(models.Model):
    _inherit = "purchase.order"
    
    _columns = {
                "catatan_gudang":fields7.Text("Catatan Untuk Gudang")
                }
    
#     def button_confirm(self, cr, uid, ids, context):
#         super(Purchase, self).button_confirm(cr,uid,ids,context)
# #         import ipdb;ipdb.set_trace()
#         obj_picking = self.pool.get("stock.picking")
#         stock_pickings = obj_picking.search(cr,uid,[("purchase_id","=", ids[0])])
#         for picking in obj_picking.browse(cr,uid,stock_pickings):
#             picking.note = self.browse(cr,uid,ids).notes
      
    @api.multi
    def button_confirm(self):
        super(Purchase, self).button_confirm()
#         import ipdb;ipdb.set_trace()
        obj_picking = self.env["stock.picking"]
        stock_pickings = obj_picking.search([("purchase_id","=",self.id)])
        for picking in stock_pickings:
            picking.note = self.notes
         