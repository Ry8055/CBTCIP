# CipherByte Python Task 
# paymentreceipt generator 
# by --> Ravi Yadav

from reportlab.pdfgen import canvas

# Define the sender information
sender_name = "Ravi Yadav"
sender_address = "CipherByte Intern"

# Prompt the user for the customer details
receiver_name = input("Enter the customer's name: ")
receiver_address = input("Enter the customer's address: ")

# Prompt the user for the payment details
payment_date = input("Enter the payment date (YYYY-MM-DD): ")
payment_amount = float(input("Enter the payment amount: "))
payment_method = input("Enter the payment method: ")

# Create a new PDF document
pdf = canvas.Canvas("payment_receipt.pdf")

# Add the receiver and sender information
pdf.setFont("Helvetica", 12)
pdf.drawString(50, 750, f"Payment Receipt")
pdf.drawString(50, 725, f"To: {receiver_name}")
pdf.drawString(50, 700, f"{receiver_address}")
pdf.drawString(50, 675, f"From: {sender_name}")
pdf.drawString(50, 650, f"{sender_address}")

# Add the payment details
pdf.drawString(50, 625, f"Date: {payment_date}")
pdf.drawString(50, 600, f"Amount: ${payment_amount:.2f}")
pdf.drawString(50, 575, f"Method: {payment_method}")

# Save the PDF document
pdf.save()