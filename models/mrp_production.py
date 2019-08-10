from odoo import api, fields, models, _


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    sw_remark = fields.Char('Remarks')


class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    sw_produce_location = fields.Selection(
        string=u'Produce Location',
        selection=[('in', 'In House'), ('out', 'Subcontract')]
    )

    # sale order related field
    sale_order_id = fields.Many2one(
        string=u'Sale Order',
        comodel_name='sale.order',
        ondelete='set null',
    )
    sale_partner_id = fields.Many2one(
        string=u'Customer',
        related="sale_order_id.partner_id",
        store=True
    )
    sale_user_id = fields.Many2one(
        string="SO Created by",
        comodel_name='res.users',
        ondelete="set null",
        related="sale_order_id.user_id",
        store=True

    )
    sale_expected_date = fields.Date(
        related="sale_order_id.exp_ship_date", store=True)
    sw_so_no = fields.Char(related="sale_order_id.sw_so_no", store=True)
    so_notes = fields.Char(related="sale_order_id.so_notes", store=True)
    special_intruction = fields.Text(
        related="sale_order_id.special_intruction", store=True)

    purchase_order_id = fields.Many2one(
        string=u'Purchase Order',
        comodel_name='purchase.order',
        ondelete='set null',
    )

    # product related field
    product_image_medium = fields.Binary(
        related="product_id.image_medium", store=True)
    barcode = fields.Char(related="product_id.barcode", store=True)
    pattern = fields.Char(related="product_id.pattern", store=True)
    prod_label = fields.Char(related="product_id.label", store=True)
    prod_ht = fields.Char(related="product_id.ht", store=True)

    # genral information tab
    product_image_detail_1 = fields.Binary(
        related="product_id.product_image_detail_1", store=True)
    product_image_detail_2 = fields.Binary(
        related="product_id.product_image_detail_2", store=True)
    product_image_detail_3 = fields.Binary(
        related="product_id.product_image_detail_3", store=True)
    product_image_detail_4 = fields.Binary(
        related="product_id.product_image_detail_4", store=True)
    product_image_detail_5 = fields.Binary(
        related="product_id.product_image_detail_5", store=True)
    product_image_detail_6 = fields.Binary(
        related="product_id.product_image_detail_6", store=True)

    # weight & size
    sm_weight = fields.Float(related="product_id.sm_weight", store=True)
    skin_weight = fields.Float(related="product_id.skin_weight", store=True)
    cotton_weight = fields.Float(
        related="product_id.cotton_weight", store=True)
    sponge_weight = fields.Float(
        related="product_id.sponge_weight", store=True)
    bean_bag_weight = fields.Float(
        related="product_id.bean_bag_weight", store=True)
    etc_weight = fields.Float(related="product_id.etc_weight", store=True)
    sm_size = fields.Float(related="product_id.sm_size", store=True)

    # sewing & finishing image
    product_specs_image_1 = fields.Binary(
        related="product_id.product_specs_image_1", store=True)
    product_specs_image_2 = fields.Binary(
        related="product_id.product_specs_image_2", store=True)
    product_specs_image_3 = fields.Binary(
        related="product_id.product_specs_image_3", store=True)

    # label
    label_no = fields.Char(related="product_id.label_no", store=True)
    label_image_1 = fields.Binary(
        related="product_id.label_image_1", store=True)
    label_image_2 = fields.Binary(
        related="product_id.label_image_2", store=True)
    label_image_3 = fields.Binary(
        related="product_id.label_image_3", store=True)
    label_image_4 = fields.Binary(
        related="product_id.label_image_4", store=True)
    label_image_5 = fields.Binary(
        related="product_id.label_image_5", store=True)

    # ht image
    ht_image_1 = fields.Binary(related="product_id.ht_image_1", store=True)
    ht_image_2 = fields.Binary(related="product_id.ht_image_2", store=True)
    ht_image_3 = fields.Binary(related="product_id.ht_image_3", store=True)
    ht_image_4 = fields.Binary(related="product_id.ht_image_4", store=True)
    ht_image_5 = fields.Binary(related="product_id.ht_image_5", store=True)

    # packing
    ctn_size = fields.Char(related="product_id.ctn_size", store=True)
    qty_per_carton = fields.Integer(
        related="product_id.qty_per_carton", store=True)
    carton_quality = fields.Char(
        related="product_id.carton_quality", store=True)
    carton_weight = fields.Float(
        related="product_id.carton_weight", store=True)
    carton_color = fields.Char(related="product_id.carton_color", store=True)
    qty_per_inner = fields.Integer(
        related="product_id.qty_per_inner", store=True)
    inner_size = fields.Char(related="product_id.inner_size", store=True)
    code_inner = fields.Char(related="product_id.code_inner", store=True)
    code_master = fields.Char(related="product_id.code_master", store=True)
    carton_marking = fields.Text(
        related="product_id.carton_marking", store=True)
    pallet_width = fields.Float(related="product_id.pallet_width", store=True)
    pallet_length = fields.Float(
        related="product_id.pallet_length", store=True)
    pallet_height = fields.Float(
        related="product_id.pallet_height", store=True)

    # Pallet
    qty_carton_per_pallet = fields.Integer(
        related="product_id.qty_carton_per_pallet", store=True)
    qty_item_per_pallet = fields.Integer(
        related="product_id.qty_item_per_pallet", store=True)
    pallet_quality = fields.Char(
        related="product_id.pallet_quality", store=True)
    pallet_weight = fields.Float(
        related="product_id.pallet_weight", store=True)
    pallet_color = fields.Char(related="product_id.pallet_color", store=True)
    pallet_feet_pattern = fields.Binary(
        related="product_id.pallet_feet_pattern", store=True)

    # etc image
    etc_image_1 = fields.Binary(related="product_id.etc_image_1", store=True)
    etc_image_2 = fields.Binary(related="product_id.etc_image_2", store=True)
    etc_image_3 = fields.Binary(related="product_id.etc_image_3", store=True)
    etc_image_4 = fields.Binary(related="product_id.etc_image_4", store=True)
    etc_image_5 = fields.Binary(related="product_id.etc_image_5", store=True)
    etc_image_6 = fields.Binary(related="product_id.etc_image_6", store=True)

    # Barcode & Sticker
    barcode_sticker_image_1 = fields.Binary(
        related="product_id.barcode_sticker_image_1", store=True)
    barcode_sticker_image_2 = fields.Binary(
        related="product_id.barcode_sticker_image_2", store=True)
    barcode_sticker_image_3 = fields.Binary(
        related="product_id.barcode_sticker_image_3", store=True)
    barcode_sticker_image_4 = fields.Binary(
        related="product_id.barcode_sticker_image_4", store=True)
    barcode_sticker_image_5 = fields.Binary(
        related="product_id.barcode_sticker_image_5", store=True)
    barcode_sticker_image_6 = fields.Binary(
        related="product_id.barcode_sticker_image_6", store=True)
