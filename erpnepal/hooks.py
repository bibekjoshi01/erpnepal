app_name = "erpnepal"
app_title = "ERPNepal"
app_publisher = "Bibek Joshi"
app_description = """ERP made simple"""
app_icon = "fa fa-th"
app_color = "#e74c3c"
app_email = "bibekjoshi34@gmailcom"
app_license = "GNU General Public License (v3)"
source_link = "https://github.com/bibekjoshi01/erp-nepal"
app_logo_url = "/assets/erpnepal/images/erpnepal-logo.svg"
app_home = "/desk"

add_to_apps_screen = [
    {
        "name": app_name,
        "logo": "/assets/erpnepal/images/erpnepal-logo.svg",
        "title": app_title,
        "route": app_home,
        "has_permission": "erpnepal.check_app_permission",
    }
]

develop_version = "17.x.x-develop"

app_include_js = "erpnepal.bundle.js"
app_include_css = "erpnepal.bundle.css"
web_include_css = "erpnepal-web.bundle.css"
email_css = "email_erpnepal.bundle.css"

app_include_icons = [
    "/assets/erpnepal/icons/pos-icons.svg",
]

web_include_icons = [
    "/assets/erpnepal/icons/pos-icons.svg",
]

doctype_js = {
    "Address": "public/js/address.js",
    "Communication": "public/js/communication.js",
    "Event": "public/js/event.js",
    "Newsletter": "public/js/newsletter.js",
    "Contact": "public/js/contact.js",
}
doctype_list_js = {
    "Code List": [
        "edi/doctype/code_list/code_list_import.js",
    ],
    "Common Code": [
        "edi/doctype/code_list/code_list_import.js",
    ],
}

page_js = {"print": "public/js/print.js"}

extend_doctype_class = {"Address": "erpnepal.accounts.custom.address.ERPNepalAddress"}

override_whitelisted_methods = {
    "frappe.www.contact.send_message": "erpnepal.templates.utils.send_message"
}

welcome_email = "erpnepal.setup.utils.welcome_email"

# setup wizard
setup_wizard_requires = "assets/erpnepal/js/setup_wizard.js"
setup_wizard_stages = "erpnepal.setup.setup_wizard.setup_wizard.get_setup_stages"
setup_wizard_complete = "erpnepal.setup.setup_wizard.setup_wizard.setup_demo"
setup_wizard_test = (
    "erpnepal.setup.setup_wizard.test_setup_wizard.run_setup_wizard_test"
)

after_install = "erpnepal.setup.install.after_install"

boot_session = "erpnepal.startup.boot.boot_session"
notification_config = "erpnepal.startup.notifications.get_notification_config"
get_help_messages = "erpnepal.utilities.activation.get_help_messages"
leaderboards = "erpnepal.startup.leaderboard.get_leaderboards"
filters_config = "erpnepal.startup.filters.get_filters_config"
additional_print_settings = "erpnepal.controllers.print_settings.get_print_settings"

on_session_creation = "erpnepal.portal.utils.create_customer_or_supplier"

treeviews = [
    "Account",
    "Cost Center",
    "Warehouse",
    "Item Group",
    "Customer Group",
    "Supplier Group",
    "Sales Person",
    "Territory",
    "Department",
]

demo_master_doctypes = [
    "item_group",
    "item",
    "customer_group",
    "supplier_group",
    "customer",
    "supplier",
]
demo_transaction_doctypes = [
    "purchase_order",
    "sales_order",
]

jinja = {
    "methods": [
        "erpnepal.stock.serial_batch_bundle.get_serial_or_batch_nos",
    ],
}

# website
webform_list_context = (
    "erpnepal.controllers.website_list_for_contact.get_webform_list_context"
)

calendars = ["Task", "Work Order", "Sales Order", "Holiday List", "ToDo"]

website_generators = ["BOM", "Sales Partner"]

website_context = {
    "favicon": "/assets/erpnepal/images/erpnepal-favicon.svg",
    "splash_image": "/assets/erpnepal/images/erpnepal-logo.svg",
}

# nosemgrep
website_route_rules = [
    {"from_route": "/orders", "to_route": "Sales Order"},
    {
        "from_route": "/orders/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Sales Order",
            "parents": [{"label": "Orders", "route": "orders"}],
        },
    },
    {"from_route": "/invoices", "to_route": "Sales Invoice"},
    {
        "from_route": "/invoices/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Sales Invoice",
            "parents": [{"label": "Invoices", "route": "invoices"}],
        },
    },
    {"from_route": "/supplier-quotations", "to_route": "Supplier Quotation"},
    {
        "from_route": "/supplier-quotations/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Supplier Quotation",
            "parents": [
                {"label": "Supplier Quotation", "route": "supplier-quotations"}
            ],
        },
    },
    {"from_route": "/purchase-orders", "to_route": "Purchase Order"},
    {
        "from_route": "/purchase-orders/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Purchase Order",
            "parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
        },
    },
    {
        "from_route": "/purchase-orders/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Purchase Order",
            "parents": [{"label": "Purchase Order", "route": "purchase-orders"}],
        },
    },
    {"from_route": "/purchase-invoices", "to_route": "Purchase Invoice"},
    {
        "from_route": "/purchase-invoices/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Purchase Invoice",
            "parents": [{"label": "Purchase Invoice", "route": "purchase-invoices"}],
        },
    },
    {"from_route": "/quotations", "to_route": "Quotation"},
    {
        "from_route": "/quotations/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Quotation",
            "parents": [{"label": "Quotations", "route": "quotations"}],
        },
    },
    {"from_route": "/shipments", "to_route": "Delivery Note"},
    {
        "from_route": "/shipments/<path:name>",
        "to_route": "order",
        "defaults": {
            "doctype": "Delivery Note",
            "parents": [{"label": "Shipments", "route": "shipments"}],
        },
    },
    {"from_route": "/rfq", "to_route": "Request for Quotation"},
    {
        "from_route": "/rfq/<path:name>",
        "to_route": "rfq",
        "defaults": {
            "doctype": "Request for Quotation",
            "parents": [{"label": "Request for Quotation", "route": "rfq"}],
        },
    },
    {"from_route": "/addresses", "to_route": "Address"},
    {
        "from_route": "/addresses/<path:name>",
        "to_route": "addresses",
        "defaults": {
            "doctype": "Address",
            "parents": [{"label": "Addresses", "route": "addresses"}],
        },
    },
    {"from_route": "/boms", "to_route": "BOM"},
    {"from_route": "/timesheets", "to_route": "Timesheet"},
    {"from_route": "/material-requests", "to_route": "Material Request"},
    {
        "from_route": "/material-requests/<path:name>",
        "to_route": "material_request_info",
        "defaults": {
            "doctype": "Material Request",
            "parents": [{"label": "Material Request", "route": "material-requests"}],
        },
    },
    {"from_route": "/project", "to_route": "Project"},
    {"from_route": "/tasks", "to_route": "Task"},
]

standard_portal_menu_items = [
    {
        "title": "Projects",
        "route": "/project",
        "reference_doctype": "Project",
        "role": "Customer",
    },
    {
        "title": "Request for Quotations",
        "route": "/rfq",
        "reference_doctype": "Request for Quotation",
        "role": "Supplier",
    },
    {
        "title": "Supplier Quotation",
        "route": "/supplier-quotations",
        "reference_doctype": "Supplier Quotation",
        "role": "Supplier",
    },
    {
        "title": "Purchase Orders",
        "route": "/purchase-orders",
        "reference_doctype": "Purchase Order",
        "role": "Supplier",
    },
    {
        "title": "Purchase Invoices",
        "route": "/purchase-invoices",
        "reference_doctype": "Purchase Invoice",
        "role": "Supplier",
    },
    {
        "title": "Quotations",
        "route": "/quotations",
        "reference_doctype": "Quotation",
        "role": "Customer",
    },
    {
        "title": "Orders",
        "route": "/orders",
        "reference_doctype": "Sales Order",
        "role": "Customer",
    },
    {
        "title": "Invoices",
        "route": "/invoices",
        "reference_doctype": "Sales Invoice",
        "role": "Customer",
    },
    {
        "title": "Shipments",
        "route": "/shipments",
        "reference_doctype": "Delivery Note",
        "role": "Customer",
    },
    {
        "title": "Issues",
        "route": "/issues",
        "reference_doctype": "Issue",
        "role": "Customer",
    },
    {"title": "Addresses", "route": "/addresses", "reference_doctype": "Address"},
    {
        "title": "Timesheets",
        "route": "/timesheets",
        "reference_doctype": "Timesheet",
        "role": "Customer",
    },
    {"title": "Newsletter", "route": "/newsletters", "reference_doctype": "Newsletter"},
    {
        "title": "Material Request",
        "route": "/material-requests",
        "reference_doctype": "Material Request",
        "role": "Customer",
    },
    {"title": "Appointment Booking", "route": "/book_appointment"},
]

sounds = [
    {
        "name": "incoming-call",
        "src": "/assets/erpnepal/sounds/incoming-call.mp3",
        "volume": 0.2,
    },
    {
        "name": "call-disconnect",
        "src": "/assets/erpnepal/sounds/call-disconnect.mp3",
        "volume": 0.2,
    },
    {
        "name": "numpad-touch",
        "src": "/assets/erpnepal/sounds/numpad-touch.mp3",
        "volume": 0.8,
    },
]

has_upload_permission = {
    "Employee": "erpnepal.setup.doctype.employee.employee.has_upload_permission"
}

has_website_permission = {
    "Sales Order": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Quotation": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Sales Invoice": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Supplier Quotation": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Purchase Order": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Purchase Invoice": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Material Request": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Delivery Note": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Issue": "erpnepal.support.doctype.issue.issue.has_website_permission",
    "Timesheet": "erpnepal.controllers.website_list_for_contact.has_website_permission",
    "Project": "erpnepal.controllers.website_list_for_contact.has_website_permission",
}

before_tests = "erpnepal.setup.utils.before_tests"


period_closing_doctypes = [
    "Sales Invoice",
    "Purchase Invoice",
    "Journal Entry",
    "Bank Clearance",
    "Stock Entry",
    "Dunning",
    "Invoice Discounting",
    "Payment Entry",
    "Period Closing Voucher",
    "Process Deferred Accounting",
    "Asset",
    "Asset Capitalization",
    "Asset Repair",
    "Delivery Note",
    "Landed Cost Voucher",
    "Purchase Receipt",
    "Stock Reconciliation",
    "Subcontracting Receipt",
]

doc_events = {
    "*": {
        "validate": [
            "erpnepal.support.doctype.service_level_agreement.service_level_agreement.apply",
            "erpnepal.setup.doctype.transaction_deletion_record.transaction_deletion_record.check_for_running_deletion_job",
        ],
    },
    tuple(period_closing_doctypes): {
        "validate": "erpnepal.accounts.doctype.accounting_period.accounting_period.validate_accounting_period_on_doc_save",
    },
    "Stock Entry": {
        "on_submit": "erpnepal.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
        "on_cancel": "erpnepal.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
    },
    "User": {
        "after_insert": "frappe.contacts.doctype.contact.contact.update_contact",
        "validate": "erpnepal.setup.doctype.employee.employee.validate_employee_role",
        "on_update": "erpnepal.portal.utils.set_default_role",
    },
    "Communication": {
        "on_update": [
            "erpnepal.support.doctype.service_level_agreement.service_level_agreement.on_communication_update",
            "erpnepal.support.doctype.issue.issue.set_first_response_time",
        ],
        "after_insert": [
            "erpnepal.crm.utils.link_communications_with_prospect",
            "erpnepal.crm.utils.update_modified_timestamp",
        ],
    },
    "Event": {
        "after_insert": "erpnepal.crm.utils.link_events_with_prospect",
    },
    "Sales Invoice": {
        "on_submit": [
            "erpnepal.regional.italy.utils.sales_invoice_on_submit",
        ],
        "on_cancel": [
            "erpnepal.regional.italy.utils.sales_invoice_on_cancel",
        ],
        "on_trash": "erpnepal.regional.check_deletion_permission",
    },
    "Purchase Invoice": {
        "validate": [
            "erpnepal.regional.united_arab_emirates.utils.update_grand_total_for_rcm",
            "erpnepal.regional.united_arab_emirates.utils.validate_returns",
        ]
    },
    "Payment Entry": {
        "on_trash": "erpnepal.regional.check_deletion_permission",
    },
    "Address": {
        "validate": [
            "erpnepal.regional.italy.utils.set_state_code",
        ],
    },
    "Contact": {
        "on_trash": "erpnepal.support.doctype.issue.issue.update_issue",
        "after_insert": "erpnepal.telephony.doctype.call_log.call_log.link_existing_conversations",
        "validate": ["erpnepal.crm.utils.update_lead_phone_numbers"],
    },
    "Email Unsubscribe": {
        "after_insert": "erpnepal.crm.doctype.email_campaign.email_campaign.unsubscribe_recipient"
    },
    "Integration Request": {
        "validate": "erpnepal.accounts.doctype.payment_request.payment_request.validate_payment"
    },
}

# function should expect the variable and doc as arguments
naming_series_variables = {
    "FY": "erpnepal.accounts.utils.parse_naming_series_variable",
    "ABBR": "erpnepal.accounts.utils.parse_naming_series_variable",
}

# On cancel event Payment Entry will be exempted and all linked submittable doctype will get cancelled.
# to maintain data integrity we exempted payment entry. it will un-link when sales invoice get cancelled.
# if payment entry not in auto cancel exempted doctypes it will cancel payment entry.
auto_cancel_exempted_doctypes = [
    "Payment Entry",
]

scheduler_events = {
    "cron": {
        "0/15 * * * *": [
            "erpnepal.manufacturing.doctype.bom_update_log.bom_update_log.resume_bom_cost_update_jobs",
        ],
        "0/30 * * * *": [
            "erpnepal.stock.doctype.repost_item_valuation.repost_item_valuation.run_parallel_reposting",
        ],
        # Hourly but offset by 30 minutes
        "30 * * * *": [
            "erpnepal.accounts.doctype.gl_entry.gl_entry.rename_gle_sle_docs",
        ],
        # Daily but offset by 45 minutes
        "45 0 * * *": [],
    },
    "hourly": [
        "erpnepal.projects.doctype.project.project.hourly_reminder",
    ],
    "hourly_long": [],
    "hourly_maintenance": [
        "erpnepal.stock.doctype.repost_item_valuation.repost_item_valuation.repost_entries",
        "erpnepal.utilities.bulk_transaction.retry",
        "erpnepal.projects.doctype.project.project.collect_project_status",
        "erpnepal.projects.doctype.project.project.project_status_update_reminder",
        "erpnepal.erpnepal_integrations.doctype.plaid_settings.plaid_settings.automatic_synchronization",
        "erpnepal.utilities.doctype.video.video.update_youtube_data",
    ],
    "daily": [],
    "daily_long": [],
    "daily_maintenance": [
        "erpnepal.support.doctype.issue.issue.auto_close_tickets",
        "erpnepal.crm.doctype.opportunity.opportunity.auto_close_opportunity",
        "erpnepal.controllers.accounts_controller.update_invoice_status",
        "erpnepal.accounts.doctype.fiscal_year.fiscal_year.auto_create_fiscal_year",
        "erpnepal.projects.doctype.task.task.set_tasks_as_overdue",
        "erpnepal.stock.doctype.serial_no.serial_no.update_maintenance_status",
        "erpnepal.buying.doctype.supplier_scorecard.supplier_scorecard.refresh_scorecards",
        "erpnepal.setup.doctype.company.company.cache_companies_monthly_sales_history",
        "erpnepal.assets.doctype.asset.asset.update_maintenance_status",
        "erpnepal.assets.doctype.asset.asset.make_post_gl_entry",
        "erpnepal.crm.doctype.contract.contract.update_status_for_contracts",
        "erpnepal.projects.doctype.project.project.update_project_sales_billing",
        "erpnepal.projects.doctype.project.project.send_project_status_email_to_users",
        "erpnepal.quality_management.doctype.quality_review.quality_review.review",
        "erpnepal.support.doctype.service_level_agreement.service_level_agreement.check_agreement_status",
        "erpnepal.crm.doctype.email_campaign.email_campaign.send_email_to_leads_or_contacts",
        "erpnepal.crm.doctype.email_campaign.email_campaign.set_email_campaign_status",
        "erpnepal.selling.doctype.quotation.quotation.set_expired_status",
        "erpnepal.buying.doctype.supplier_quotation.supplier_quotation.set_expired_status",
        "erpnepal.accounts.doctype.process_statement_of_accounts.process_statement_of_accounts.send_auto_email",
        "erpnepal.accounts.utils.auto_create_exchange_rate_revaluation_daily",
        "erpnepal.accounts.utils.run_ledger_health_checks",
        "erpnepal.assets.doctype.asset_maintenance_log.asset_maintenance_log.update_asset_maintenance_log_status",
        "erpnepal.stock.reorder_item.reorder_item",
        "erpnepal.accounts.doctype.process_subscription.process_subscription.create_subscription_process",
        "erpnepal.setup.doctype.email_digest.email_digest.send",
        "erpnepal.manufacturing.doctype.bom_update_tool.bom_update_tool.auto_update_latest_price_in_all_boms",
        "erpnepal.crm.utils.open_leads_opportunities_based_on_todays_event",
        "erpnepal.assets.doctype.asset.depreciation.post_depreciation_entries",
    ],
    "weekly": [
        "erpnepal.accounts.utils.auto_create_exchange_rate_revaluation_weekly",
    ],
    "monthly_long": [
        "erpnepal.accounts.deferred_revenue.process_deferred_accounting",
        "erpnepal.accounts.utils.auto_create_exchange_rate_revaluation_monthly",
    ],
}

email_brand_image = "assets/erpnepal/images/erpnepal-logo.jpg"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://frappe.io/erpnepal?source=via_email_footer" target="_blank">
			ERPNepal
		</a>
	</span>
"""

get_translated_dict = {
    ("doctype", "Global Defaults"): "frappe.geo.country_info.get_translated_dict"
}

bot_parsers = [
    "erpnepal.utilities.bot.FindItemBot",
]

get_site_info = "erpnepal.utilities.get_site_info"

payment_gateway_enabled = "erpnepal.accounts.utils.create_payment_gateway_account"

communication_doctypes = ["Customer", "Supplier"]

advance_payment_receivable_doctypes = ["Sales Order"]
advance_payment_payable_doctypes = ["Purchase Order"]

invoice_doctypes = ["Sales Invoice", "Purchase Invoice"]

bank_reconciliation_doctypes = [
    "Payment Entry",
    "Journal Entry",
    "Purchase Invoice",
    "Sales Invoice",
]

accounting_dimension_doctypes = [
    "GL Entry",
    "Payment Ledger Entry",
    "Sales Invoice",
    "Purchase Invoice",
    "Payment Entry",
    "Asset",
    "Stock Entry",
    "Budget",
    "Delivery Note",
    "Sales Invoice Item",
    "Purchase Invoice Item",
    "Purchase Order Item",
    "Sales Order Item",
    "Journal Entry Account",
    "Material Request Item",
    "Delivery Note Item",
    "Purchase Receipt Item",
    "Stock Entry Detail",
    "Payment Entry Deduction",
    "Sales Taxes and Charges",
    "Purchase Taxes and Charges",
    "Shipping Rule",
    "Landed Cost Item",
    "Asset Value Adjustment",
    "Asset Repair",
    "Asset Capitalization",
    "Loyalty Program",
    "Stock Reconciliation",
    "POS Profile",
    "Opening Invoice Creation Tool",
    "Opening Invoice Creation Tool Item",
    "Subscription",
    "Subscription Plan",
    "POS Invoice",
    "POS Invoice Item",
    "Purchase Order",
    "Purchase Receipt",
    "Sales Order",
    "Subcontracting Order",
    "Subcontracting Order Item",
    "Subcontracting Receipt",
    "Subcontracting Receipt Item",
    "Account Closing Balance",
    "Supplier Quotation",
    "Supplier Quotation Item",
    "Payment Reconciliation",
    "Payment Reconciliation Allocation",
    "Payment Request",
    "Asset Movement Item",
    "Asset Depreciation Schedule",
    "Advance Taxes and Charges",
]

get_matching_queries = "erpnepal.accounts.doctype.bank_reconciliation_tool.bank_reconciliation_tool.get_matching_queries"

get_amounts_not_reflected_in_system_for_bank_reconciliation_statement = "erpnepal.accounts.report.bank_reconciliation_statement.bank_reconciliation_statement.get_amounts_not_reflected_in_system_for_bank_reconciliation_statement"

get_payment_entries_for_bank_clearance = "erpnepal.accounts.doctype.bank_clearance.bank_clearance.get_payment_entries_for_bank_clearance"

get_entries_for_bank_clearance_summary = "erpnepal.accounts.report.bank_clearance_summary.bank_clearance_summary.get_entries_for_bank_clearance_summary"

get_entries_for_bank_reconciliation_statement = "erpnepal.accounts.report.bank_reconciliation_statement.bank_reconciliation_statement.get_entries_for_bank_reconciliation_statement"

regional_overrides = {
    "France": {
        "erpnepal.tests.test_regional.test_method": "erpnepal.regional.france.utils.test_method"
    },
    "United Arab Emirates": {
        "erpnepal.controllers.taxes_and_totals.update_itemised_tax_data": "erpnepal.regional.united_arab_emirates.utils.update_itemised_tax_data",
        "erpnepal.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries": "erpnepal.regional.united_arab_emirates.utils.make_regional_gl_entries",
    },
    "Saudi Arabia": {
        "erpnepal.controllers.taxes_and_totals.update_itemised_tax_data": "erpnepal.regional.united_arab_emirates.utils.update_itemised_tax_data"
    },
    "Italy": {
        "erpnepal.controllers.taxes_and_totals.update_itemised_tax_data": "erpnepal.regional.italy.utils.update_itemised_tax_data",
        "erpnepal.controllers.accounts_controller.validate_regional": "erpnepal.regional.italy.utils.sales_invoice_validate",
    },
}
user_privacy_documents = [
    {
        "doctype": "Lead",
        "match_field": "email_id",
        "personal_fields": ["phone", "mobile_no", "fax", "website", "lead_name"],
    },
    {
        "doctype": "Opportunity",
        "match_field": "contact_email",
        "personal_fields": ["contact_mobile", "contact_display", "customer_name"],
    },
]


# ERPNepal doctypes for Global Search
global_search_doctypes = {
    "Default": [
        {"doctype": "Customer", "index": 0},
        {"doctype": "Supplier", "index": 1},
        {"doctype": "Item", "index": 2},
        {"doctype": "Warehouse", "index": 3},
        {"doctype": "Account", "index": 4},
        {"doctype": "Employee", "index": 5},
        {"doctype": "BOM", "index": 6},
        {"doctype": "Sales Invoice", "index": 7},
        {"doctype": "Sales Order", "index": 8},
        {"doctype": "Quotation", "index": 9},
        {"doctype": "Work Order", "index": 10},
        {"doctype": "Purchase Order", "index": 11},
        {"doctype": "Purchase Receipt", "index": 12},
        {"doctype": "Purchase Invoice", "index": 13},
        {"doctype": "Delivery Note", "index": 14},
        {"doctype": "Stock Entry", "index": 15},
        {"doctype": "Material Request", "index": 16},
        {"doctype": "Delivery Trip", "index": 17},
        {"doctype": "Pick List", "index": 18},
        {"doctype": "Payment Entry", "index": 22},
        {"doctype": "Lead", "index": 23},
        {"doctype": "Opportunity", "index": 24},
        {"doctype": "Item Price", "index": 25},
        {"doctype": "Purchase Taxes and Charges Template", "index": 26},
        {"doctype": "Sales Taxes and Charges", "index": 27},
        {"doctype": "Asset", "index": 28},
        {"doctype": "Project", "index": 29},
        {"doctype": "Task", "index": 30},
        {"doctype": "Timesheet", "index": 31},
        {"doctype": "Issue", "index": 32},
        {"doctype": "Serial No", "index": 33},
        {"doctype": "Batch", "index": 34},
        {"doctype": "Branch", "index": 35},
        {"doctype": "Department", "index": 36},
        {"doctype": "Designation", "index": 38},
        {"doctype": "Maintenance Schedule", "index": 45},
        {"doctype": "Maintenance Visit", "index": 46},
        {"doctype": "Warranty Claim", "index": 47},
    ],
}

ignore_links_on_delete = [
    "Tax Withholding Entry",
]

additional_timeline_content = {
    "*": ["erpnepal.telephony.doctype.call_log.call_log.get_linked_call_logs"]
}


extend_bootinfo = [
    "erpnepal.support.doctype.service_level_agreement.service_level_agreement.add_sla_doctypes",
    "erpnepal.startup.boot.bootinfo",
]


default_log_clearing_doctypes = {
    "Repost Item Valuation": 60,
}


export_python_type_annotations = True

fields_for_group_similar_items = ["qty", "amount"]

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
ignore_translatable_strings_from = ["frappe"]
