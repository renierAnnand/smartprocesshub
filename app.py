import streamlit as st
import pandas as pd
from datetime import datetime, date

# Page configuration
st.set_page_config(
    page_title="Business Process Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simple CSS for better appearance
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
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
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
    
    .status-active {
        background: #c6f6d5;
        color: #22543d;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        display: inline-block;
    }
    
    .status-beta {
        background: #fed7d7;
        color: #742a2a;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        display: inline-block;
    }
    
    .status-new {
        background: #bee3f8;
        color: #2a4365;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        display: inline-block;
    }
    
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 8px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

def show_dashboard():
    """Display the main dashboard"""
    
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
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">👤</div>
                <div class="card-title">New Hire</div>
                <div class="card-description">Streamline employee onboarding with automated workflows and document collection.</div>
            </div>
            <div><span class="status-active">Active</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open New Hire Form", key="new_hire", use_container_width=True):
            st.session_state.current_page = 'new_hire'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏢</div>
                <div class="card-title">Customer/Vendor Creation</div>
                <div class="card-description">Register new customers and vendors with comprehensive profile setup and verification.</div>
            </div>
            <div><span class="status-active">Active</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Customer/Vendor Form", key="customer_creation", use_container_width=True):
            st.session_state.current_page = 'customer_creation'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📋</div>
                <div class="card-title">PO Request</div>
                <div class="card-description">Submit and track purchase order requests with approval workflow.</div>
            </div>
            <div><span class="status-active">Active</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open PO Request", key="po_request", use_container_width=True):
            st.session_state.current_page = 'po_request'
            st.rerun()
    
    # Row 2
    with col1:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">💰</div>
                <div class="card-title">Invoice Processing</div>
                <div class="card-description">Automate invoice validation, approval, and payment processing.</div>
            </div>
            <div><span class="status-beta">Beta</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Invoice Processing", key="invoice_processing", use_container_width=True):
            st.session_state.current_page = 'invoice_processing'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">💳</div>
                <div class="card-title">Expense Report</div>
                <div class="card-description">Submit and manage expense claims with receipt attachment and approval flow.</div>
            </div>
            <div><span class="status-active">Active</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Expense Report", key="expense_report", use_container_width=True):
            st.session_state.current_page = 'expense_report'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏖️</div>
                <div class="card-title">Leave Request</div>
                <div class="card-description">Request time off with calendar integration and manager approval workflow.</div>
            </div>
            <div><span class="status-active">Active</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Leave Request", key="leave_request", use_container_width=True):
            st.session_state.current_page = 'leave_request'
            st.rerun()
    
    # Row 3
    with col1:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🖥️</div>
                <div class="card-title">Asset Management</div>
                <div class="card-description">Track and manage company assets with assignment and maintenance schedules.</div>
            </div>
            <div><span class="status-new">New</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Asset Management", key="asset_management", use_container_width=True):
            st.session_state.current_page = 'asset_management'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📄</div>
                <div class="card-title">Contract Review</div>
                <div class="card-description">Submit contracts for legal review with collaborative editing and approval.</div>
            </div>
            <div><span class="status-beta">Beta</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Contract Review", key="contract_review", use_container_width=True):
            st.session_state.current_page = 'contract_review'
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">⭐</div>
                <div class="card-title">Performance Review</div>
                <div class="card-description">Conduct employee performance evaluations with 360-degree feedback collection.</div>
            </div>
            <div><span class="status-new">New</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Performance Review", key="performance_review", use_container_width=True):
            st.session_state.current_page = 'performance_review'
            st.rerun()
    
    # Row 4 - New Processes
    with col1:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔄</div>
                <div class="card-title">Internal Transfer</div>
                <div class="card-description">Process employee department transfers and role changes with approval workflow.</div>
            </div>
            <div><span class="status-new">New</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Internal Transfer", key="internal_transfer", use_container_width=True):
            st.session_state.current_page = 'internal_transfer'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="process-card">
            <div>
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🚀</div>
                <div class="card-title">Project Initiation</div>
                <div class="card-description">Submit new project proposals with budget requests and approval routing.</div>
            </div>
            <div><span class="status-new">New</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Open Project Initiation", key="project_initiation", use_container_width=True):
            st.session_state.current_page = 'project_initiation'
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
            full_name = st.text_input("Full Name *")
            national_id = st.text_input("National ID / Passport Number *")
            dob = st.date_input("Date of Birth *")
            job_title = st.text_input("Job Title *")
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"])
        
        with col2:
            joining_date = st.date_input("Joining Date *")
            salary_grade = st.text_input("Salary / Grade *")
            work_location = st.text_input("Work Location *")
            manager = st.text_input("Manager *")
        
        st.subheader("📎 Attachments")
        col1, col2, col3 = st.columns(3)
        with col1:
            id_document = st.file_uploader("ID Document *", type=['pdf', 'jpg', 'png'])
        with col2:
            resume = st.file_uploader("Resume *", type=['pdf', 'doc', 'docx'])
        with col3:
            offer_letter = st.file_uploader("Offer Letter *", type=['pdf', 'doc', 'docx'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
                if all([full_name, national_id, dob, job_title, department, joining_date, salary_grade, work_location, manager]):
                    st.success("✅ New Hire request submitted successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields marked with *")

def show_customer_creation_form():
    """Customer/Vendor Creation process form"""
    st.markdown("## 🏢 Customer/Vendor Creation")
    
    if st.button("← Back to Dashboard", key="back_customer"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("customer_creation_form"):
        # Entity Type Selection
        entity_type = st.selectbox("Entity Type *", ["", "Customer", "Vendor"])
        
        col1, col2 = st.columns(2)
        
        with col1:
            entity_name = st.text_input("Entity Name (Customer/Vendor) *")
            tax_id = st.text_input("Tax ID / VAT Number *")
            contact_name = st.text_input("Primary Contact Name *")
            contact_email = st.text_input("Contact Email *")
        
        with col2:
            contact_phone = st.text_input("Contact Phone *")
            payment_terms = st.selectbox("Payment Terms *", 
                                       ["", "Net 30", "Net 60", "Net 90", 
                                        "Advance Payment", "Cash on Delivery"])
            credit_limit = st.number_input("Credit Limit *", min_value=0.0)
        
        company_address = st.text_area("Company Address *")
        
        st.subheader("💳 Bank Details")
        col1, col2 = st.columns(2)
        with col1:
            bank_name = st.text_input("Bank Name")
            account_number = st.text_input("Account Number")
        with col2:
            swift_code = st.text_input("SWIFT/IBAN Code")
            account_holder = st.text_input("Account Holder Name")
        
        st.subheader("📎 Attachments")
        col1, col2 = st.columns(2)
        with col1:
            company_license = st.file_uploader("Company License *", type=['pdf', 'jpg', 'png'])
        with col2:
            tax_certificate = st.file_uploader("Tax Certificate *", type=['pdf', 'jpg', 'png'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
                if all([entity_type, entity_name, tax_id, contact_name, contact_email, contact_phone, payment_terms, company_address]):
                    st.success(f"✅ {entity_type} creation request submitted successfully!")
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
            requestor_name = st.text_input("Requestor Name *")
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"])
            supplier_name = st.text_input("Supplier Name *")
            quantity = st.number_input("Quantity *", min_value=1)
        
        with col2:
            unit_price = st.number_input("Unit Price *", min_value=0.0, step=0.01)
            delivery_date = st.date_input("Delivery Date *")
            budget_code = st.text_input("Budget Code / GL Account *")
        
        item_description = st.text_area("Item Description *")
        justification = st.text_area("Justification *")
        
        st.subheader("📎 Attachments")
        col1, col2 = st.columns(2)
        with col1:
            quotation = st.file_uploader("Quotation", type=['pdf', 'doc', 'docx'])
        with col2:
            tech_spec = st.file_uploader("Technical Specification", type=['pdf', 'doc', 'docx'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
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
            supplier_name = st.text_input("Supplier Name *")
            invoice_number = st.text_input("Invoice Number *")
            invoice_date = st.date_input("Invoice Date *")
            amount = st.number_input("Amount *", min_value=0.0, step=0.01)
        
        with col2:
            currency = st.selectbox("Currency *", 
                                  ["", "SAR - Saudi Riyal", "USD - US Dollar", 
                                   "EUR - Euro", "GBP - British Pound"])
            po_reference = st.text_input("PO Reference")
            gl_account = st.text_input("Cost Center / GL Account *")
        
        st.subheader("📎 Attachments")
        col1, col2 = st.columns(2)
        with col1:
            invoice_pdf = st.file_uploader("Invoice PDF *", type=['pdf'])
        with col2:
            delivery_note = st.file_uploader("Delivery Note", type=['pdf', 'jpg', 'png'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Invoice", type="primary", use_container_width=True):
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
            employee_name = st.text_input("Employee Name *")
            employee_id = st.text_input("Employee ID *")
            expense_type = st.selectbox("Expense Type *", 
                                      ["", "Travel", "Meals & Entertainment", "Office Supplies", 
                                       "Transportation", "Accommodation", "Training & Education", "Other"])
        
        with col2:
            expense_date = st.date_input("Expense Date *")
            amount = st.number_input("Amount *", min_value=0.0, step=0.01)
            cost_center = st.text_input("Cost Center *")
        
        description = st.text_area("Description *")
        
        st.subheader("📎 Receipt")
        receipt = st.file_uploader("Upload Receipt *", type=['pdf', 'jpg', 'png'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Report", type="primary", use_container_width=True):
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
            employee_name = st.text_input("Employee Name *")
            employee_id = st.text_input("Employee ID *")
            leave_type = st.selectbox("Leave Type *", 
                                    ["", "Annual Leave", "Sick Leave", "Emergency Leave", 
                                     "Maternity Leave", "Paternity Leave", "Unpaid Leave"])
            start_date = st.date_input("Start Date *")
        
        with col2:
            end_date = st.date_input("End Date *")
            backup_person = st.text_input("Backup Person *")
            manager_name = st.text_input("Manager Name", placeholder="Auto-filled if available")
        
        reason = st.text_area("Reason for Leave *")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
                if all([employee_name, employee_id, leave_type, start_date, end_date, backup_person, reason]):
                    st.success("✅ Leave request submitted successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields marked with *")

def show_asset_management_form():
    """Asset Assignment / Transfer form"""
    st.markdown("## 🖥️ Asset Assignment / Transfer")
    
    if st.button("← Back to Dashboard", key="back_asset"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("asset_management_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            asset_type = st.selectbox("Asset Type *", 
                                    ["", "Laptop", "Desktop Computer", "Monitor", 
                                     "Mobile Phone", "Printer", "Furniture", "Vehicle", "Other"])
            requestor_name = st.text_input("Requestor Name *")
            quantity = st.number_input("Quantity *", min_value=1)
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"])
        
        with col2:
            desired_delivery_date = st.date_input("Desired Delivery Date *")
            current_location = st.text_input("Current Location")
            assigned_to = st.text_input("Assigned To")
        
        purpose_justification = st.text_area("Purpose / Justification *")
        
        st.subheader("📎 Attachments")
        asset_tag = st.file_uploader("Asset Tag (Optional)", type=['pdf', 'jpg', 'png'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
                if all([asset_type, requestor_name, quantity, department, desired_delivery_date, purpose_justification]):
                    st.success("✅ Asset request submitted successfully!")
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
            employee_name = st.text_input("Employee Name *")
            reviewer_name = st.text_input("Reviewer Name *")
            review_period = st.text_input("Review Period *", placeholder="e.g., Q1 2025")
        
        with col2:
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"])
            final_rating = st.selectbox("Final Rating *", 
                                      ["", "Outstanding", "Exceeds Expectations", 
                                       "Meets Expectations", "Below Expectations", "Unsatisfactory"])
        
        kpis = st.text_area("KPIs / Objectives *")
        strengths = st.text_area("Strengths *")
        improvements = st.text_area("Areas for Improvement *")
        feedback_360 = st.text_area("360 Feedback (Optional)")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Review", type="primary", use_container_width=True):
                if all([employee_name, reviewer_name, review_period, department, final_rating, kpis, strengths, improvements]):
                    st.success("✅ Performance review submitted successfully!")
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
            contract_title = st.text_input("Contract Title *")
            initiator_name = st.text_input("Initiator Name *")
            business_unit = st.selectbox("Business Unit *", 
                                       ["", "Corporate", "Sales", "Operations", 
                                        "Finance", "Human Resources", "Information Technology"])
            legal_contact = st.text_input("Legal Contact *")
        
        with col2:
            start_date = st.date_input("Start Date *")
            end_date = st.date_input("End Date *")
            contract_type = st.selectbox("Type of Contract *", 
                                       ["", "NDA (Non-Disclosure Agreement)", "Vendor Agreement", 
                                        "Partnership Agreement", "Service Agreement", 
                                        "Employment Contract", "Other"])
        
        parties_involved = st.text_area("Parties Involved *")
        
        st.subheader("📎 Attachments")
        draft_contract = st.file_uploader("Upload Draft Contract *", type=['pdf', 'doc', 'docx'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Review", type="primary", use_container_width=True):
                if all([contract_title, initiator_name, business_unit, legal_contact, start_date, end_date, contract_type, parties_involved]):
                    st.success("✅ Contract review request submitted successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields marked with *")

def show_internal_transfer_form():
    """Internal Transfer / Employee Change form"""
    st.markdown("## 🔄 Internal Transfer / Employee Change")
    
    if st.button("← Back to Dashboard", key="back_internal_transfer"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("internal_transfer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            employee_name = st.text_input("Employee Name *")
            current_department = st.selectbox("Current Department *", 
                                            ["", "Human Resources", "Information Technology", 
                                             "Finance", "Marketing", "Sales", "Operations"])
            new_department = st.selectbox("New Department *", 
                                        ["", "Human Resources", "Information Technology", 
                                         "Finance", "Marketing", "Sales", "Operations"])
            new_manager = st.text_input("New Manager *")
        
        with col2:
            new_job_title = st.text_input("New Job Title *")
            effective_date = st.date_input("Effective Date *")
            salary_adjustment = st.number_input("Salary Adjustment (if any)", value=0.0, step=0.01)
            hr_approval = st.text_input("HR Approval", placeholder="Auto-routed")
        
        reason_for_change = st.text_area("Reason for Change *")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
                if all([employee_name, current_department, new_department, new_manager, new_job_title, effective_date, reason_for_change]):
                    st.success("✅ Internal transfer request submitted successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields marked with *")

def show_project_initiation_form():
    """Project Initiation / Budget Request form"""
    st.markdown("## 🚀 Project Initiation / Budget Request")
    
    if st.button("← Back to Dashboard", key="back_project_initiation"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    with st.form("project_initiation_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            project_name = st.text_input("Project Name *")
            requestor = st.text_input("Requestor *")
            department = st.selectbox("Department *", 
                                    ["", "Human Resources", "Information Technology", 
                                     "Finance", "Marketing", "Sales", "Operations"])
            estimated_budget = st.number_input("Estimated Budget *", min_value=0.0, step=0.01)
        
        with col2:
            start_date = st.date_input("Start Date *")
            end_date = st.date_input("End Date *")
            gl_account = st.text_input("GL Account / Budget Code *")
            approval_path = st.text_input("Approval Path", placeholder="Auto-routed")
        
        business_justification = st.text_area("Business Justification *")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("💾 Save Draft", use_container_width=True):
                st.info("💾 Draft saved successfully!")
        with col2:
            if st.form_submit_button("🚀 Submit Request", type="primary", use_container_width=True):
                if all([project_name, requestor, department, estimated_budget, start_date, end_date, gl_account, business_justification]):
                    st.success("✅ Project initiation request submitted successfully!")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields marked with *")

def main():
    """Main application logic"""
    
    # Sidebar for navigation (optional)
    with st.sidebar:
        st.markdown("### 🏢 Navigation")
        if st.button("🏠 Dashboard"):
            st.session_state.current_page = 'dashboard'
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
    elif st.session_state.current_page == 'internal_transfer':
        show_internal_transfer_form()
    elif st.session_state.current_page == 'project_initiation':
        show_project_initiation_form()

if __name__ == "__main__":
    main()
