#!/usr/bin/env python3
"""
Atelier 8 - Luxury Restoration Dashboard
Python Data Analytics & Export Script
"""

import csv
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class AtelierDashboard:
    def __init__(self, data_dir="public/data"):
        self.data_dir = Path(data_dir)
        self.customers = self._load_csv("customers.csv")
        self.services = self._load_csv("services.csv")
        self.orders = self._load_csv("orders.csv")
        self.memberships = self._load_csv("memberships.csv")
        self.inventory = self._load_csv("inventory.csv")
        self.auth_records = self._load_csv("authentication_records.csv")
        self.revenue = self._load_csv("revenue.csv")

    def _load_csv(self, filename):
        """Load CSV file and return as list of dictionaries"""
        try:
            with open(self.data_dir / filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            print(f"Warning: {filename} not found")
            return []

    def get_dashboard_stats(self):
        """Calculate key dashboard statistics"""
        total_customers = len(self.customers)
        active_orders = sum(1 for o in self.orders if o['status'] == 'In Progress')
        completed_orders = sum(1 for o in self.orders if o['status'] == 'Completed')
        active_memberships = sum(1 for m in self.memberships if m['status'] == 'Active')

        total_revenue = sum(float(r['total_revenue_aed']) for r in self.revenue)
        avg_satisfaction = sum(float(o['satisfaction_score']) for o in self.orders if o['satisfaction_score']) / completed_orders if completed_orders > 0 else 0

        auth_pass = sum(1 for a in self.auth_records if a['overall_result'] == 'Authentic')
        auth_rate = (auth_pass / len(self.auth_records)) * 100 if self.auth_records else 0

        return {
            'total_customers': total_customers,
            'active_orders': active_orders,
            'completed_orders': completed_orders,
            'active_memberships': active_memberships,
            'total_revenue': total_revenue,
            'avg_satisfaction': round(avg_satisfaction, 1),
            'authentication_rate': round(auth_rate, 1),
        }

    def get_customer_segments(self):
        """Group customers by segment"""
        segments = defaultdict(list)
        for customer in self.customers:
            segments[customer['segment']].append(customer)
        return dict(segments)

    def get_revenue_by_month(self):
        """Get revenue breakdown by month"""
        return [
            {
                'month': r['month'],
                'service_revenue': int(r['service_revenue_aed']),
                'membership_revenue': int(r['membership_revenue_aed']),
                'resale_commission': int(r['resale_commission_aed']),
                'total_revenue': int(r['total_revenue_aed']),
            }
            for r in self.revenue
        ]

    def get_service_utilization(self):
        """Calculate which services are most used"""
        service_usage = defaultdict(int)
        for order in self.orders:
            service_ids = order['service_ids'].split(',')
            for service_id in service_ids:
                service_id = service_id.strip()
                for service in self.services:
                    if service['service_id'] == service_id:
                        service_usage[service['service_name']] += 1
        return sorted(service_usage.items(), key=lambda x: x[1], reverse=True)

    def get_inventory_status(self):
        """Check inventory levels"""
        low_stock = []
        for item in self.inventory:
            if int(item['current_stock']) <= int(item['reorder_level']):
                low_stock.append({
                    'material_id': item['material_id'],
                    'material_name': item['material_name'],
                    'current_stock': int(item['current_stock']),
                    'reorder_level': int(item['reorder_level']),
                    'status': 'LOW STOCK - REORDER NOW'
                })
        return low_stock

    def get_customer_ltv_analysis(self):
        """Analyze customer lifetime value by segment"""
        segment_analysis = {}
        for segment, customers in self.get_customer_segments().items():
            total_ltv = sum(float(c['ltv']) for c in customers)
            avg_ltv = total_ltv / len(customers) if customers else 0
            segment_analysis[segment] = {
                'count': len(customers),
                'total_ltv': total_ltv,
                'avg_ltv': round(avg_ltv, 0),
            }
        return segment_analysis

    def generate_report(self):
        """Generate complete dashboard report"""
        print("\n" + "="*70)
        print("ATELIER 8 - LUXURY RESTORATION DASHBOARD REPORT")
        print("="*70)

        # Dashboard Stats
        print("\n📊 DASHBOARD STATISTICS")
        print("-" * 70)
        stats = self.get_dashboard_stats()
        for key, value in stats.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")

        # Customer Segments
        print("\n👥 CUSTOMER SEGMENTS")
        print("-" * 70)
        segments = self.get_customer_segments()
        for segment, customers in segments.items():
            print(f"  {segment}: {len(customers)} customers")

        # Revenue Analysis
        print("\n💰 MONTHLY REVENUE")
        print("-" * 70)
        revenue = self.get_revenue_by_month()
        for month_data in revenue:
            print(f"  {month_data['month']}: {month_data['total_revenue']:,} AED")

        # Service Utilization
        print("\n🔧 TOP SERVICES")
        print("-" * 70)
        services = self.get_service_utilization()
        for service, count in services[:5]:
            print(f"  {service}: {count} orders")

        # Inventory Status
        print("\n📦 INVENTORY STATUS")
        print("-" * 70)
        low_stock = self.get_inventory_status()
        if low_stock:
            for item in low_stock:
                print(f"  ⚠️  {item['material_name']}: {item['current_stock']} units")
        else:
            print("  ✅ All inventory levels normal")

        # Customer LTV
        print("\n💎 CUSTOMER LTV BY SEGMENT")
        print("-" * 70)
        ltv_analysis = self.get_customer_ltv_analysis()
        for segment, analysis in ltv_analysis.items():
            print(f"  {segment}:")
            print(f"    Count: {analysis['count']} | Avg LTV: {analysis['avg_ltv']:,.0f} AED")

        print("\n" + "="*70 + "\n")

    def export_to_json(self, filename="dashboard_data.json"):
        """Export all data to JSON"""
        data = {
            'timestamp': datetime.now().isoformat(),
            'dashboard_stats': self.get_dashboard_stats(),
            'customer_segments': self.get_customer_segments(),
            'revenue_analysis': self.get_revenue_by_month(),
            'service_utilization': self.get_service_utilization(),
            'inventory_status': self.get_inventory_status(),
            'customer_ltv_analysis': self.get_customer_ltv_analysis(),
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Data exported to {filename}")


def main():
    """Main execution"""
    # Initialize dashboard
    dashboard = AtelierDashboard()

    # Generate report
    dashboard.generate_report()

    # Export JSON
    dashboard.export_to_json()


if __name__ == "__main__":
    main()
