from .api.accounts import Accounts
from .api.classifications import Classifications
from .api.departments import Departments
from .api.currencies import Currencies
from .api.locations import Locations
from .api.vendor_bills import VendorBills
from .api.vendors import Vendors
from .api.subsidiaries import Subsidiaries
from .api.journal_entries import JournalEntries
from .api.employees import Employees
from .api.expense_reports import ExpenseReports
from .api.folders import Folders
from .api.files import Files
from .api.expense_categories import ExpenseCategory
from .api.custom_lists import CustomLists
from .api.custom_records import CustomRecords
from .api.vendor_payments import VendorPayments
from .internal.client import NetSuiteClient


class NetSuiteConnection:
    def __init__(self, account, consumer_key, consumer_secret, token_key, token_secret, cache_settings=None):
        """
        :param str account: The account ID
        :param str consumer_key: Netsuite Consumer Key
        :param str consumer_secret: Netsuite Consumer Secret
        :param str token_key: Netsuite Token Key
        :param str token_secret: Netsuite Token Secret
        :param dict cache_settings: Cache Settings for NetSuiteClient
        """
        ns_client = NetSuiteClient(account=account, caching=cache_settings)
        ns_client.connect_tba(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            token_key=token_key,
            token_secret=token_secret
        )
        self.client = ns_client
        self.accounts = Accounts(ns_client)
        self.classifications = Classifications(ns_client)
        self.departments = Departments(ns_client)
        self.currencies = Currencies(ns_client)
        self.locations = Locations(ns_client)
        self.vendor_bills = VendorBills(ns_client)
        self.vendors = Vendors(ns_client)
        self.subsidiaries = Subsidiaries(ns_client)
        self.journal_entries = JournalEntries(ns_client)
        self.employees = Employees(ns_client)
        self.expense_reports = ExpenseReports(ns_client)
        self.folders = Folders(ns_client)
        self.files = Files(ns_client)
        self.expense_categories = ExpenseCategory(ns_client)
        self.custom_lists = CustomLists(ns_client)
        self.custom_records = CustomRecords(ns_client)
        self.vendor_payments = VendorPayments(ns_client)
