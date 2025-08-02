"""
Bank Account Command Line Interface
"""

import argparse
import sys
from bank_account import BankAccount, InsufficientFundsError, InvalidAmountError

def create_argument_parser():
    parser = argparse.ArgumentParser(
        description="Bank Account Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --name "John Doe" --balance 1000 --deposit 500
  python main.py --name "Jane Smith" --balance 1000 --withdraw 200
"""
    )
    parser.add_argument('--name', required=True, help='Account holder name')
    parser.add_argument('--balance', type=float, default=0, help='Initial balance')
    parser.add_argument('--deposit', type=float, help='Amount to deposit')
    parser.add_argument('--withdraw', type=float, help='Amount to withdraw')
    parser.add_argument('--check', action='store_true', help='Check current balance')
    parser.add_argument('--info', action='store_true', help='Display account information')
    return parser

def perform_operations(account, args):
    done = False

    if args.deposit is not None:
        try:
            account.deposit(args.deposit)
            done = True
        except (InvalidAmountError, ValueError) as e:
            print(f"Deposit failed: {e}")
            return False

    if args.withdraw is not None:
        try:
            account.withdraw(args.withdraw)
            done = True
        except (InvalidAmountError, InsufficientFundsError, ValueError) as e:
            print(f"Withdrawal failed: {e}")
            return False

    if args.check:
        account.check_balance()
        done = True

    if args.info:
        account.get_account_info()
        done = True

    if not done:
        print("Account created.")
        account.check_balance()
        print("Use --help for options.")

    return True

def main():
    print("Bank Account Management System\n" + "="*40)
    parser = create_argument_parser()

    try:
        args = parser.parse_args()
    except SystemExit:
        return

    try:
        print(f"Creating account for: {args.name}")
        account = BankAccount(args.name, args.balance)

        if perform_operations(account, args):
            print(f"Session complete. Final account: {account}")
            print("="*40)
        else:
            print("Session terminated due to error.")
            sys.exit(1)

    except InvalidAmountError as e:
        print(f"Invalid Amount: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Value Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
