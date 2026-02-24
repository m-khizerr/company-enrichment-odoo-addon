from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ------------------------------------------------------------------
    # Helper: provides the DB id of the "Company Keywords" parent tag
    # so the view can filter category_id and set default_parent_id.
    # This is module infrastructure only — not replicated in Studio.
    # ------------------------------------------------------------------
    keyword_parent_id = fields.Integer(
        compute='_compute_keyword_parent_id',
    )

    @api.depends_context('company')
    def _compute_keyword_parent_id(self):
        parent = self.env.ref(
            'company_enrichment.tag_company_keywords',
            raise_if_not_found=False,
        )
        val = parent.id if parent else 0
        for rec in self:
            rec.keyword_parent_id = val

    # ------------------------------------------------------------------
    # Target Account
    # ------------------------------------------------------------------
    x_is_target_account = fields.Boolean(
        string='Target Account',
        default=False,
        tracking=True,
    )

    # ------------------------------------------------------------------
    # Warehouse / Receiving
    # ------------------------------------------------------------------
    x_dock_information = fields.Selection(
        [
            ('commercial', 'Commercial Loading Dock'),
            ('liftgate', 'Lift Gate Needed'),
            ('ups', 'Ships UPS'),
            ('no_dock_forklift', 'No Commercial Dock | Forklift on Site'),
            ('forklift_required', 'Forklift Required'),
        ],
        string='Dock Information',
    )

    x_receiving_hours = fields.Text(
        string='Receiving Hours',
    )

    x_delivery_appointment_details = fields.Selection(
        [
            ('no_appt', 'No Appointments | First Come First Served'),
            ('call_30min', 'Call 30 min prior'),
            ('call_1hr', 'Call 1 hour prior'),
            ('call_24hr', 'Call 24 hours prior'),
            ('call_48hr', 'Call 48 hours prior'),
            ('call_72hr', 'Call 72 hours prior'),
        ],
        string='Delivery Appointment Details',
    )

    # ------------------------------------------------------------------
    # Social / Profile URLs
    # ------------------------------------------------------------------
    x_linkedin_url = fields.Char(string='LinkedIn URL')
    x_instagram_url = fields.Char(string='Instagram URL')
    x_facebook_url = fields.Char(string='Facebook URL')
    x_youtube_url = fields.Char(string='YouTube URL')

    # ------------------------------------------------------------------
    # Company Profile (optional)
    # ------------------------------------------------------------------
    x_year_founded = fields.Integer(string='Year Founded')
    x_employee_count = fields.Integer(string='Employee Count')
    x_revenue_range = fields.Selection(
        [
            ('lt_1m', 'Less than $1M'),
            ('1m_10m', '$1M - $10M'),
            ('10m_50m', '$10M - $50M'),
            ('50m_100m', '$50M - $100M'),
            ('100m_500m', '$100M - $500M'),
            ('gt_500m', '$500M+'),
        ],
        string='Revenue Range',
    )
