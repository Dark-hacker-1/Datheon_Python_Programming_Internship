import csv
import sys

def get_portfolio_inputs():
    portfolio = []
    print("=" * 50)
    print("STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 50)
    print("Enter your stock holdings (type 'done' when finished).")
    
    while True:
        ticker = input("\nEnter stock ticker symbol (e.g., AAPL, TSLA) or 'done': ").strip().upper()
        if ticker == 'DONE':
            break
        if not ticker:
            print("Ticker cannot be empty. Try again.")
            continue
            
        try:
            shares = float(input(f"Enter number of shares for {ticker}: "))
            buy_price = float(input(f"Enter purchase price per share for {ticker} ($): "))
            current_price = float(input(f"Enter current market price per share for {ticker} ($): "))
        except ValueError:
            print("Invalid number entered. Please use numeric values for shares and prices.")
            continue
            
        portfolio.append({
            "ticker": ticker,
            "shares": shares,
            "buy_price": buy_price,
            "current_price": current_price
        })
        
    return portfolio

def calculate_performance(portfolio):
    updated_portfolio = []
    total_invested = 0.0
    total_current_value = 0.0
    
    for item in portfolio:
        invested = item["shares"] * item["buy_price"]
        current_val = item["shares"] * item["current_price"]
        gain_loss = current_val - invested
        gain_loss_pct = (gain_loss / invested) * 100 if invested > 0 else 0.0
        
        total_invested += invested
        total_current_value += current_val
        
        updated_portfolio.append({
            "ticker": item["ticker"],
            "shares": item["shares"],
            "buy_price": item["buy_price"],
            "current_price": item["current_price"],
            "invested_value": round(invested, 2),
            "current_value": round(current_val, 2),
            "gain_loss": round(gain_loss, 2),
            "gain_loss_pct": round(gain_loss_pct, 2)
        })
        
    total_gain_loss = total_current_value - total_invested
    total_gain_loss_pct = (total_gain_loss / total_invested) * 100 if total_invested > 0 else 0.0
    
    summary = {
        "holdings": updated_portfolio,
        "total_invested": round(total_invested, 2),
        "total_current_value": round(total_current_value, 2),
        "total_gain_loss": round(total_gain_loss, 2),
        "total_gain_loss_pct": round(total_gain_loss_pct, 2)
    }
    
    return summary

def save_to_csv(summary, filename="portfolio_summary.csv"):
    try:
        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = ['Ticker', 'Shares', 'Buy Price', 'Current Price', 'Total Invested', 'Current Value', 'Gain/Loss ($)', 'Gain/Loss (%)']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in summary["holdings"]:
                writer.writerow({
                    'Ticker': item['ticker'],
                    'Shares': item['shares'],
                    'Buy Price': item['buy_price'],
                    'Current Price': item['current_price'],
                    'Total Invested': item['invested_value'],
                    'Current Value': item['current_value'],
                    'Gain/Loss ($)': item['gain_loss'],
                    'Gain/Loss (%)': item['gain_loss_pct']
                })
            
            # Write total summary rows at the bottom
            writer.writerow({})
            writer.writerow({'Ticker': 'TOTAL PORTFOLIO', 'Current Value': summary['total_current_value'], 'Gain/Loss ($)': summary['total_gain_loss']})
            
        print(f"\n[Success] Portfolio summary successfully exported to '{filename}'.")
    except Exception as e:
        print(f"Error saving file: {e}")

def display_summary(summary):
    print("\n" + "=" * 60)
    print("PORTFOLIO PERFORMANCE REPORT")
    print("=" * 60)
    print(f"{'Ticker':<10} {'Shares':<10} {'Invested':<12} {'Current Val':<12} {'Gain/Loss':<12}")
    print("-" * 60)
    
    for item in summary["holdings"]:
        print(f"{item['ticker']:<10} {item['shares']:<10} ${item['invested_value']:<11.2f} ${item['current_value']:<11.2f} ${item['gain_loss']:<11.2f} ({item['gain_loss_pct']:+.2f}%)")
        
    print("-" * 60)
    print(f"Total Invested Capital:   ${summary['total_invested']:.2f}")
    print(f"Total Current Valuation:  ${summary['total_current_value']:.2f}")
    print(f"Net Gain / Loss:          ${summary['total_gain_loss']:.2f} ({summary['total_gain_loss_pct']:+.2f}%)")
    print("=" * 60)

if __name__ == "__main__":
    portfolio_data = get_portfolio_inputs()
    if portfolio_data:
        portfolio_summary = calculate_performance(portfolio_data)
        display_summary(portfolio_summary)
        save_to_csv(portfolio_summary)
    else:
        print("No stocks entered.")
      
