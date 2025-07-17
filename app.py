import streamlit as st
import pandas as pd
from datetime import datetime, date
import base64

# Page configuration
st.set_page_config(
    page_title="Business Process Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .process-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
        transition: transform 0.2s;
        cursor: pointer;
    }
    
    .process-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
    }
    
    .card-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .card-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .card-description {
        color: #718096;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
    }
    
    .status-active {
        background: #c6f6d5;
        color: #22543d;
    }
    
    .status-beta {
        background: #fed7d7;
        color: #742a2a;
    }
    
    .status-new {
        background: #bee3f8;
        color: #2a4365;
    }
    
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    
    .back-button {
        background: #6c757d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

def show_dashboard():
    """Display the main dashboard with process cards"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏢 Business Process Dashboard</h1>
        <p>Select a process to get started</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Process cards in a grid layout
    col1, col2, col3 = st.columns(3)
    
    # Row 1
    with col1:
        if st.button("👤 New Hire", key="new_hire", help="Employee onboarding process"):
            st.session_state.current_page = 'new_hire'
            st.rerun()
    
    with col2:
        if st.button("🏢 Customer Creation", key="customer_creation", help="Register new customers"):
            st.session_state.current_page = 'customer_creation'
            st.rerun()
    
    with col3:
        if st.button("📋 PO Request", key="po_request", help="Purchase order requests"):
            st.session_state.current_page = 'po_request'
            st.rerun()
    
    # Row 2
    with col1:
        if st.button("💰 Invoice Processing", key="invoice_processing", help="Invoice validation and processing"):
            st.session_state.current_page = 'invoice_processing'
            st.rerun()
    
    with col2:
        if st.button("💳 Expense Report", key="expense_report", help="Expense claims and reimbursements"):
            st.session_state.current_page = 'expense_report'
            st.rerun()
    
    with col3:
        if st.button("🏖️ Leave Request", key="leave_request", help="Time off requests"):
            st.session_state.current_page = 'leave_request'
            st.rerun()
    
    # Row 3
    with col1:
        if st.button("🖥️ Asset Management", key="asset_management", help="Company asset tracking"):
            st.session_state.current_page = 'asset_management'
            st.rerun()
    
    with col2:
        if st.button("📄 Contract Review", key="contract_review", help="Legal contract processing"):
            st.session_state.current_page = 'contract_review'
            st.rerun()
    
    with col3:
        if st.button("⭐ Performance Review", key="performance_review", help="Employee evaluations"):
            st.session_state.current_page = 'performance_review'
            st.rerun()

def show_new_hire_form():
    """New Hire process form"""
    st.markdown("## 👤 New Hire Process")
    
    if st.button("← Back to Dashboard", key="back_new_hire"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("new_hire_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Full Name *", key="nh_full_name")
            national_id = st.text_input("National ID / Passport Number *", key="nh_national_id")
            dob = st.date_input("Date of Birth *", key="nh_dob")
            job_title = st.text_input("Job Title *", key="nh_job_title")
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"], key="nh_department")
        
        with col2:
            joining_date = st.date_input("Joining Date *", key="nh_joining_date")
            salary_grade = st.text_input("Salary / Grade *", key="nh_salary")
            work_location = st.text_input("Work Location *", key="nh_location")
            manager = st.text_input("Manager *", key="nh_manager")
        
        st.subheader("Attachments")
        col1, col2, col3 = st.columns(3)
        with col1:
            id_document = st.file_uploader("ID Document *", type=['pdf', 'jpg', 'png'], key="nh_id")
        with col2:
            resume = st.file_uploader("Resume *", type=['pdf', 'doc', 'docx'], key="nh_resume")
        with col3:
            offer_letter = st.file_uploader("Offer Letter *", type=['pdf', 'doc', 'docx'], key="nh_offer")
        
        submitted = st.form_submit_button("Submit New Hire Request", type="primary")
        
        if submitted:
            if all([full_name, national_id, dob, job_title, department, joining_date, salary_grade, work_location, manager]):
                st.success("✅ New Hire request submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_customer_creation_form():
    """Customer Creation process form"""
    st.markdown("## 🏢 Customer Creation")
    
    if st.button("← Back to Dashboard", key="back_customer"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("customer_creation_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            company_name = st.text_input("Company Name *", key="cc_company")
            vat_id = st.text_input("VAT / Tax ID *", key="cc_vat")
            industry = st.selectbox("Industry Type *", 
                                  ["", "Technology", "Healthcare", "Finance", 
                                   "Manufacturing", "Retail", "Construction", "Other"], key="cc_industry")
            contact_name = st.text_input("Contact Person Name *", key="cc_contact_name")
        
        with col2:
            contact_email = st.text_input("Contact Email *", key="cc_email")
            contact_phone = st.text_input("Contact Phone *", key="cc_phone")
            payment_terms = st.selectbox("Payment Terms *", 
                                       ["", "Net 30", "Net 60", "Net 90", 
                                        "Advance Payment", "Cash on Delivery"], key="cc_payment")
            credit_limit = st.number_input("Credit Limit *", min_value=0.0, key="cc_credit")
        
        address = st.text_area("Address *", key="cc_address")
        
        st.subheader("Attachments")
        col1, col2 = st.columns(2)
        with col1:
            commercial_reg = st.file_uploader("Commercial Registration *", type=['pdf', 'jpg', 'png'], key="cc_reg")
        with col2:
            tax_cert = st.file_uploader("Tax Certificate *", type=['pdf', 'jpg', 'png'], key="cc_tax")
        
        submitted = st.form_submit_button("Submit Customer Creation", type="primary")
        
        if submitted:
            if all([company_name, vat_id, industry, contact_name, contact_email, contact_phone, payment_terms, address]):
                st.success("✅ Customer creation request submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_po_request_form():
    """PO Request process form"""
    st.markdown("## 📋 Purchase Order Request")
    
    if st.button("← Back to Dashboard", key="back_po"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("po_request_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            requestor_name = st.text_input("Requestor Name *", key="po_requestor")
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"], key="po_department")
            supplier_name = st.text_input("Supplier Name *", key="po_supplier")
            quantity = st.number_input("Quantity *", min_value=1, key="po_quantity")
        
        with col2:
            unit_price = st.number_input("Unit Price *", min_value=0.0, step=0.01, key="po_price")
            delivery_date = st.date_input("Delivery Date *", key="po_delivery")
            budget_code = st.text_input("Budget Code / GL Account *", key="po_budget")
        
        item_description = st.text_area("Item Description *", key="po_description")
        justification = st.text_area("Justification *", key="po_justification")
        
        st.subheader("Attachments")
        col1, col2 = st.columns(2)
        with col1:
            quotation = st.file_uploader("Quotation", type=['pdf', 'doc', 'docx'], key="po_quotation")
        with col2:
            tech_spec = st.file_uploader("Technical Specification", type=['pdf', 'doc', 'docx'], key="po_spec")
        
        submitted = st.form_submit_button("Submit PO Request", type="primary")
        
        if submitted:
            if all([requestor_name, department, supplier_name, quantity, unit_price, delivery_date, budget_code, item_description, justification]):
                st.success("✅ Purchase Order request submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_invoice_processing_form():
    """Invoice Processing form"""
    st.markdown("## 💰 Invoice Processing")
    
    if st.button("← Back to Dashboard", key="back_invoice"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("invoice_processing_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            supplier_name = st.text_input("Supplier Name *", key="inv_supplier")
            invoice_number = st.text_input("Invoice Number *", key="inv_number")
            invoice_date = st.date_input("Invoice Date *", key="inv_date")
            amount = st.number_input("Amount *", min_value=0.0, step=0.01, key="inv_amount")
        
        with col2:
            currency = st.selectbox("Currency *", 
                                  ["", "SAR - Saudi Riyal", "USD - US Dollar", 
                                   "EUR - Euro", "GBP - British Pound"], key="inv_currency")
            po_reference = st.text_input("PO Reference", key="inv_po_ref")
            gl_account = st.text_input("Cost Center / GL Account *", key="inv_gl")
        
        st.subheader("Attachments")
        col1, col2 = st.columns(2)
        with col1:
            invoice_pdf = st.file_uploader("Invoice PDF *", type=['pdf'], key="inv_pdf")
        with col2:
            delivery_note = st.file_uploader("Delivery Note", type=['pdf', 'jpg', 'png'], key="inv_delivery")
        
        submitted = st.form_submit_button("Submit Invoice", type="primary")
        
        if submitted:
            if all([supplier_name, invoice_number, invoice_date, amount, currency, gl_account]):
                st.success("✅ Invoice submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_expense_report_form():
    """Expense Report form"""
    st.markdown("## 💳 Expense Report")
    
    if st.button("← Back to Dashboard", key="back_expense"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("expense_report_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            employee_name = st.text_input("Employee Name *", key="exp_name")
            employee_id = st.text_input("Employee ID *", key="exp_id")
            expense_type = st.selectbox("Expense Type *", 
                                      ["", "Travel", "Meals & Entertainment", "Office Supplies", 
                                       "Transportation", "Accommodation", "Training & Education", "Other"], key="exp_type")
        
        with col2:
            expense_date = st.date_input("Expense Date *", key="exp_date")
            amount = st.number_input("Amount *", min_value=0.0, step=0.01, key="exp_amount")
            cost_center = st.text_input("Cost Center *", key="exp_cost_center")
        
        description = st.text_area("Description *", key="exp_description")
        
        st.subheader("Receipt")
        receipt = st.file_uploader("Upload Receipt *", type=['pdf', 'jpg', 'png'], key="exp_receipt")
        
        submitted = st.form_submit_button("Submit Expense Report", type="primary")
        
        if submitted:
            if all([employee_name, employee_id, expense_type, expense_date, amount, cost_center, description]):
                st.success("✅ Expense report submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_leave_request_form():
    """Leave Request form"""
    st.markdown("## 🏖️ Leave Request")
    
    if st.button("← Back to Dashboard", key="back_leave"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("leave_request_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            employee_name = st.text_input("Employee Name *", key="leave_name")
            employee_id = st.text_input("Employee ID *", key="leave_id")
            leave_type = st.selectbox("Leave Type *", 
                                    ["", "Annual Leave", "Sick Leave", "Emergency Leave", 
                                     "Maternity Leave", "Paternity Leave", "Unpaid Leave"], key="leave_type")
            start_date = st.date_input("Start Date *", key="leave_start")
        
        with col2:
            end_date = st.date_input("End Date *", key="leave_end")
            backup_person = st.text_input("Backup Person *", key="leave_backup")
            manager_name = st.text_input("Manager Name", placeholder="Auto-filled if available", key="leave_manager")
        
        reason = st.text_area("Reason for Leave *", key="leave_reason")
        
        submitted = st.form_submit_button("Submit Leave Request", type="primary")
        
        if submitted:
            if all([employee_name, employee_id, leave_type, start_date, end_date, backup_person, reason]):
                st.success("✅ Leave request submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_asset_management_form():
    """Asset Management form"""
    st.markdown("## 🖥️ Asset Management")
    
    if st.button("← Back to Dashboard", key="back_asset"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("asset_management_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            asset_type = st.selectbox("Asset Type *", 
                                    ["", "Laptop", "Desktop Computer", "Monitor", 
                                     "Mobile Phone", "Printer", "Furniture", "Vehicle", "Other"], key="asset_type")
            requestor_name = st.text_input("Requestor Name *", key="asset_requestor")
            quantity = st.number_input("Quantity *", min_value=1, key="asset_quantity")
        
        with col2:
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"], key="asset_department")
            delivery_date = st.date_input("Desired Delivery Date *", key="asset_delivery")
            assigned_to = st.text_input("Assigned To", key="asset_assigned")
        
        justification = st.text_area("Purpose / Justification *", key="asset_justification")
        
        st.subheader("Attachments")
        request_form = st.file_uploader("Request Form (Optional)", type=['pdf', 'doc', 'docx'], key="asset_form")
        
        submitted = st.form_submit_button("Submit Asset Request", type="primary")
        
        if submitted:
            if all([asset_type, requestor_name, quantity, department, delivery_date, justification]):
                st.success("✅ Asset request submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_contract_review_form():
    """Contract Review form"""
    st.markdown("## 📄 Contract Review")
    
    if st.button("← Back to Dashboard", key="back_contract"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("contract_review_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            contract_title = st.text_input("Contract Title *", key="contract_title")
            initiator_name = st.text_input("Initiator Name *", key="contract_initiator")
            business_unit = st.selectbox("Business Unit *", 
                                       ["", "Corporate", "Sales", "Operations", 
                                        "Finance", "Human Resources", "Information Technology"], key="contract_unit")
            legal_contact = st.text_input("Legal Contact *", key="contract_legal")
        
        with col2:
            start_date = st.date_input("Start Date *", key="contract_start")
            end_date = st.date_input("End Date *", key="contract_end")
            contract_type = st.selectbox("Type of Contract *", 
                                       ["", "NDA (Non-Disclosure Agreement)", "Vendor Agreement", 
                                        "Partnership Agreement", "Service Agreement", 
                                        "Employment Contract", "Other"], key="contract_type")
        
        parties_involved = st.text_area("Parties Involved *", key="contract_parties")
        
        st.subheader("Attachments")
        draft_contract = st.file_uploader("Upload Draft Contract *", type=['pdf', 'doc', 'docx'], key="contract_draft")
        
        submitted = st.form_submit_button("Submit Contract Review", type="primary")
        
        if submitted:
            if all([contract_title, initiator_name, business_unit, legal_contact, start_date, end_date, contract_type, parties_involved]):
                st.success("✅ Contract review request submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def show_performance_review_form():
    """Performance Review form"""
    st.markdown("## ⭐ Performance Review")
    
    if st.button("← Back to Dashboard", key="back_performance"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("performance_review_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            employee_name = st.text_input("Employee Name *", key="perf_employee")
            reviewer_name = st.text_input("Reviewer Name *", key="perf_reviewer")
            review_period = st.text_input("Review Period *", placeholder="e.g., Q1 2025", key="perf_period")
        
        with col2:
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"], key="perf_department")
            final_rating = st.selectbox("Final Rating *", 
                                      ["", "Outstanding", "Exceeds Expectations", 
                                       "Meets Expectations", "Below Expectations", "Unsatisfactory"], key="perf_rating")
        
        kpis = st.text_area("KPIs / Objectives *", key="perf_kpis")
        strengths = st.text_area("Strengths *", key="perf_strengths")
        improvements = st.text_area("Areas for Improvement *", key="perf_improvements")
        feedback_360 = st.text_area("360 Feedback (Optional)", key="perf_360")
        
        submitted = st.form_submit_button("Submit Performance Review", type="primary")
        
        if submitted:
            if all([employee_name, reviewer_name, review_period, department, final_rating, kpis, strengths, improvements]):
                st.success("✅ Performance review submitted successfully!")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")

def main():
    """Main application logic"""
    
    # Sidebar for navigation (optional)
    with st.sidebar:
        st.markdown("### 🏢 Navigation")
        if st.button("🏠 Dashboard", key="sidebar_dashboard"):
            st.session_state.current_page = 'dashboard'
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Quick Links")
        if st.button("👤 New Hire", key="sidebar_new_hire"):
            st.session_state.current_page = 'new_hire'
            st.rerun()
        if st.button("🏢 Customer Creation", key="sidebar_customer"):
            st.session_state.current_page = 'customer_creation'
            st.rerun()
        if st.button("📋 PO Request", key="sidebar_po"):
            st.session_state.current_page = 'po_request'
            st.rerun()
    
    # Main content area
    if st.session_state.current_page == 'dashboard':
        show_dashboard()
    elif st.session_state.current_page == 'new_hire':
        show_new_hire_form()
    elif st.session_state.current_page == 'customer_creation':
        show_customer_creation_form()
    elif st.session_state.current_page == 'po_request':
        show_po_request_form()
    elif st.session_state.current_page == 'invoice_processing':
        show_invoice_processing_form()
    elif st.session_state.current_page == 'expense_report':
        show_expense_report_form()
    elif st.session_state.current_page == 'leave_request':
        show_leave_request_form()
    elif st.session_state.current_page == 'asset_management':
        show_asset_management_form()
    elif st.session_state.current_page == 'contract_review':
        show_contract_review_form()
    elif st.session_state.current_page == 'performance_review':
        show_performance_review_form()

if __name__ == "__main__":
    main()