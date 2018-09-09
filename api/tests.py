from django.test import TestCase
from .account import Account
from .models import RMAccount

# Create your tests here.
class AccountTests(TestCase):

    def test_get_placement_account(self):
        """
            getAccount("Placement") should return valid Placement account and there should be exactly 1
            Placement account in DB and it should match the returned account
        """
        RMAccount.objects.filter(type="Placement").delete()
        account = Account.getAccount("Placement")
        self.assertEqual(Account.checkLogin("Placement", account.username, account.password), True)
        self.assertEqual(RMAccount.objects.filter(type="Placement").count(), 1)
        if RMAccount.objects.filter(type="Placement").exists():
            db_account = RMAccount.objects.get(type="Placement")
            self.assertEqual(account, db_account)

    def test_get_internship_account(self):
        """
            getAccount("Internship") should return valid Internship account and there should be exactly 1
            Internship account in DB and it should match the returned account
        """
        RMAccount.objects.filter(type="Internship").delete()
        account = Account.getAccount("Internship")
        self.assertEqual(Account.checkLogin("Internship", account.username, account.password), True)
        self.assertEqual(RMAccount.objects.filter(type="Internship").count(), 1)
        if RMAccount.objects.filter(type="Internship").exists():
            db_account = RMAccount.objects.get(type="Internship")
            self.assertEqual(account, db_account)
