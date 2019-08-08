from odoo import fields, api, models
from datetime import datetime
from odoo import tools
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class stock_picking(models.Model):
    _inherit = "product.template"

    sw_product_type = fields.Selection(
        string=u'SW Product Type',
        selection=[('000', 'Bear'), ('010', 'Dog'), ('020', 'Cat'), ('030', 'Wild Animal'), ('040', 'Farming Animal'), ('050', 'Character'), ('060',
                                                                                                                                              'Marine Animal'), ('070', 'Household Items'), ('080', 'Hand Puppet'), ('090', 'Nursery'), ('100', 'ACC'), ('110', 'Etc'), ('012', 'Set(Assorted)')]
    )
    customer_product_code = fields.Char(string=u'Customer Product Code')
    pattern = fields.Char('Pattern')

    # genral information tab
    product_image_detail_1 = fields.Binary("Extra Image")
    product_image_detail_2 = fields.Binary("Extra Image 2")
    product_image_detail_3 = fields.Binary("Extra Image 3")
    product_image_detail_4 = fields.Binary("Extra Image 4")
    product_image_detail_5 = fields.Binary("Extra Image 5")
    product_image_detail_6 = fields.Binary("Extra Image 6")

    # weight & size
    weight_uom_text = fields.Char(default="g")
    size_uom_text = fields.Char(default="cm")
    sm_weight = fields.Float('Weight', compute="_compute_sm_weight", store=True)
    skin_weight = fields.Float('Skin Weight')
    cotton_weight = fields.Float('Cotton Weight')
    sponge_weight = fields.Float('Sponge Weight')
    bean_bag_weight = fields.Float('Bean Bag Weight')
    etc_weight = fields.Float('Etc Weigh')
    sm_size = fields.Float('Size')

    # sewing & finishing image
    product_specs_image_1 = fields.Binary("Product Spec. 1")
    product_specs_image_2 = fields.Binary("Product Spec. 2")
    product_specs_image_3 = fields.Binary("Product Spec. 3")

    # label
    label_no = fields.Char('Label No.')
    label_image_1 = fields.Binary("Label 1")
    label_image_2 = fields.Binary("Label 2")
    label_image_3 = fields.Binary("Label 3")
    label_image_4 = fields.Binary("Label 4")
    label_image_5 = fields.Binary("Label 5")

    # ht image
    ht_image_1 = fields.Binary("H/T 1")
    ht_image_2 = fields.Binary("H/T 2")
    ht_image_3 = fields.Binary("H/T 3")
    ht_image_4 = fields.Binary("H/T 4")
    ht_image_5 = fields.Binary("H/T 5")

    # packing
    ctn_size = fields.Char('CTN')
    qty_per_carton = fields.Integer('Qty/Carton')
    carton_quality = fields.Char('Carton Quality')
    carton_weight = fields.Float('Carton Weight')
    carton_color = fields.Char('Carton Color')
    qty_per_inner = fields.Integer('Qty/Inner')
    inner_size = fields.Char('Inner Size')
    code_inner = fields.Char('Code Inner')
    code_master = fields.Char('Code Master')
    carton_marking = fields.Text('Carton Marking')
    pallet_width = fields.Float('Pallet Width')
    pallet_length = fields.Float('Pallet length')
    pallet_height = fields.Float('Pallet height')

    # Pallet
    qty_carton_per_pallet = fields.Integer('Qty Ctn/Pallet')
    qty_item_per_pallet = fields.Integer('Qty Item/Pallet')
    pallet_quality = fields.Char('Pallet Quality')
    pallet_weight = fields.Float('Pallet Weight')
    pallet_color = fields.Char('Pallet Color')
    pallet_feet_pattern = fields.Binary("Pallet Feet Pattern")

    # etc image
    etc_image_1 = fields.Binary("ETC Image 1")
    etc_image_2 = fields.Binary("ETC Image 2")
    etc_image_3 = fields.Binary("ETC Image 3")
    etc_image_4 = fields.Binary("ETC Image 4")
    etc_image_5 = fields.Binary("ETC Image 5")
    etc_image_6 = fields.Binary("ETC Image 6")
    
    # Barcode & Sticker
    barcode_sticker_image_1 = fields.Binary("Barcode/Sticker Image 1")
    barcode_sticker_image_2 = fields.Binary("Barcode/Sticker Image 2")
    barcode_sticker_image_3 = fields.Binary("Barcode/Sticker Image 3")
    barcode_sticker_image_4 = fields.Binary("Barcode/Sticker Image 4")
    barcode_sticker_image_5 = fields.Binary("Barcode/Sticker Image 5")
    barcode_sticker_image_6 = fields.Binary("Barcode/Sticker Image 6")

    @api.depends('skin_weight', 'cotton_weight', 'sponge_weight', 'bean_bag_weight', 'etc_weight')
    def _compute_sm_weight(self):
        for rec in self:
            rec.sm_weight = rec.skin_weight + rec.cotton_weight + \
                rec.sponge_weight + rec.bean_bag_weight + rec.etc_weight
