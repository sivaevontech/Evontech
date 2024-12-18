# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    stock_group_id = fields.Integer(string='Stock Group ID')
    stock_unit_id = fields.Integer(string='Stock Unit ID')
    prompt_id = fields.Integer(string='Prompt ID')
    notes_id = fields.Integer(string='Notes ID')
    ratio_id = fields.Integer(string='Ratio ID')
    udf1_id = fields.Integer(string='UDF1 ID')
    udf2_id = fields.Integer(string='UDF2 ID')
    udf3_id = fields.Integer(string='UDF3 ID')
    udf4_id = fields.Integer(string='UDF4 ID')
    pack_size_popup = fields.Char(string='Pack Size Popup')
    print_components = fields.Char(string='Print Components')
    kitset = fields.Char(string='Kitset')
    internet_sequence = fields.Char(string='Internet Sequence')
    internet_short_desc = fields.Char(string='Internet Short Description')
    internet_description = fields.Char(string='Internet Description')
    information_description = fields.Char(string='Information 1 Description')
    internet_promotion = fields.Char(string='Internet Promotion')
    internet_video_url = fields.Char(string='Internet Video URL')
    internet_active = fields.Integer(string='Internet Active')
    internet_isfeatured = fields.Integer(string='Internet IsFeatured')
    label_number = fields.Integer(string='Label Number')
    gst_rate = fields.Integer(string='GST Rate')
    default_margin = fields.Integer(string='Default Margin %')
    weight = fields.Integer(string='Weight')
    volume = fields.Integer(string='Volume')
    loyalty_scheme = fields.Integer(string='Loyalty Schemes')
    weight_item = fields.Integer(string='Weighed Item')
    head_office_pricing = fields.Integer(string='Head Office Pricing')
    internet_cluster_id = fields.Integer(string='Internet Cluster ID')
    availability = fields.Integer(string='Availability')
    serial_number = fields.Integer(string='Serial Numbers')
    web_id = fields.Integer(string='Web ID')

