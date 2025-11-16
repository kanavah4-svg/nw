# 🎨 ATELIER 8 - LUXURY RESTORATION DASHBOARD

Complete production-ready Next.js dashboard with Python analytics script.

## 📦 WHAT'S INCLUDED

✅ **Frontend (React/Next.js 15)**
- Responsive dashboard with 6+ pages
- Real-time analytics & charts
- Customer management interface
- Order tracking system
- Service catalog
- Luxury design theme

✅ **Backend (Python + APIs)**
- Python app.py for data analytics
- REST API endpoints
- CSV data export functionality
- Statistical analysis

✅ **Data (7 CSV Files)**
- customers.csv (8 customers)
- services.csv (9 services)
- orders.csv (8 orders)
- memberships.csv (6 memberships)
- inventory.csv (7 materials)
- authentication_records.csv (5 records)
- revenue.csv (3 months)

✅ **Configuration Files**
- package.json (dependencies)
- tsconfig.json (TypeScript)
- tailwind.config.ts (styling)
- .gitignore (git rules)
- and more...

---

## ⚡ QUICK START

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Development Server
```bash
npm run dev
```
Open: http://localhost:3000

### 3. Run Python Analytics (Optional)
```bash
python app.py
```

### 4. Build for Production
```bash
npm run build
npm start
```

---

## 🐍 PYTHON SCRIPT (app.py)

**Features:**
- Load and analyze all CSV data
- Calculate dashboard statistics
- Generate business reports
- Export data to JSON
- Inventory analysis
- Customer LTV calculation
- Revenue breakdown

**Run it:**
```bash
python app.py
```

**Output:**
- Console report with key metrics
- dashboard_data.json file with all analytics

---

## 🌐 DEPLOYMENT

### GitHub
```bash
git init
git add .
git commit -m "Initial"
git remote add origin https://github.com/YOUR_USERNAME/atelier-8-dashboard
git branch -M main
git push -u origin main
```

### Vercel
1. Go to vercel.com
2. Import GitHub repository
3. Deploy (auto)
4. Get live URL

---

## 📂 PROJECT STRUCTURE

```
atelier-8-dashboard/
├── app.py                    # Python analytics script
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── globals.css
│   ├── api/
│   │   ├── customers/
│   │   ├── orders/
│   │   ├── services/
│   │   ├── analytics/
│   │   └── export/
│   ├── components/
│   │   ├── Sidebar.tsx
│   │   ├── Header.tsx
│   │   ├── StatCard.tsx
│   │   ├── Chart.tsx
│   │   └── DataTable.tsx
│   └── dashboard/
│       ├── page.tsx
│       ├── customers/
│       ├── orders/
│       ├── services/
│       ├── analytics/
│       └── settings/
├── lib/
│   ├── types.ts
│   └── data.ts
├── public/
│   └── data/
│       ├── customers.csv
│       ├── services.csv
│       ├── orders.csv
│       ├── memberships.csv
│       ├── inventory.csv
│       ├── authentication_records.csv
│       └── revenue.csv
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── next.config.js
└── README.md
```

---

## 🔌 API ENDPOINTS

- `GET /api/customers` - Get all customers
- `GET /api/orders?status=Completed` - Get filtered orders
- `GET /api/services?category=Restoration` - Get services
- `GET /api/analytics` - Get analytics data
- `GET /api/export?type=orders` - Export CSV

---

## 🎯 FEATURES

### Dashboard
- 4 stat cards (customers, orders, revenue, auth rate)
- Revenue trend chart (line)
- Customer segments chart (pie)
- Recent orders table

### Customers
- View all customers
- Customer segments
- Lifetime value (LTV)
- Contact information

### Orders
- Order tracking
- Status updates
- Brand information
- Satisfaction scores

### Services
- Complete service catalog
- Pricing in AED
- Duration and complexity
- Category breakdown

### Analytics
- Revenue by source
- Service utilization
- Growth metrics
- Monthly trends

### Settings
- Business configuration
- Currency selection
- Commission rates

---

## 🛠️ CUSTOMIZATION

### Change Colors
Edit `tailwind.config.ts`:
```typescript
colors: {
  atelier: {
    gold: '#d4af37',  // Change this
  }
}
```

### Add New Page
1. Create `app/dashboard/new-page/page.tsx`
2. Add to Sidebar navigation
3. Create API route if needed

### Connect Database
Replace mock data in `lib/data.ts` with database queries.

---

## 📊 DATA FILES

All CSV files are in `public/data/`:

**customers.csv**
- 8 customers with segments, income, LTV
- From your business research

**services.csv**
- 9 services with pricing in AED
- Cleaning, restoration, authentication

**orders.csv**
- 8 sample orders
- Completed and in-progress status

**memberships.csv**
- 6 active memberships
- Classic, Patron, Collector tiers

**inventory.csv**
- 7 materials and supplies
- Stock levels and reorder points

**authentication_records.csv**
- 5 authentication results
- Pass/fail for each metric

**revenue.csv**
- 3 months of revenue
- Service, membership, commission breakdown

---

## 🐍 PYTHON ANALYTICS

Run `python app.py` to get:

1. **Dashboard Statistics**
   - Total customers
   - Active orders
   - Monthly revenue
   - Authentication rate

2. **Customer Segments**
   - Count per segment
   - LTV analysis
   - Income brackets

3. **Revenue Analysis**
   - Monthly breakdown
   - Revenue sources
   - Growth trends

4. **Inventory Status**
   - Low stock alerts
   - Reorder recommendations

5. **Export to JSON**
   - dashboard_data.json with all data
   - Ready for use in other tools

---

## ✅ TESTING

### Local Testing
```bash
npm run dev
# Visit http://localhost:3000
# Test all navigation links
# Check dashboard pages
# Test API endpoints
```

### API Testing
```bash
curl http://localhost:3000/api/customers
curl http://localhost:3000/api/analytics
curl http://localhost:3000/api/export?type=orders
```

### Python Testing
```bash
python app.py
# Check console output
# Verify dashboard_data.json created
```

---

## 🚀 DEPLOYMENT CHECKLIST

Before going live:
- [ ] npm install successful
- [ ] npm run dev works
- [ ] All pages load
- [ ] Charts display
- [ ] Python script runs
- [ ] Git repo created
- [ ] Pushed to GitHub
- [ ] Vercel deployment successful
- [ ] Live URL working
- [ ] All features tested

---

## 📞 TROUBLESHOOTING

**npm install fails**
- Delete `node_modules/` and try again
- Clear npm cache: `npm cache clean --force`

**Port 3000 in use**
- Use different port: `npm run dev -- -p 3001`

**Python script errors**
- Check Python version: `python --version`
- Ensure CSV files in `public/data/`

**Charts not displaying**
- Check browser console for errors
- Verify Recharts installed

**Vercel deployment fails**
- Check build logs in Vercel dashboard
- Ensure all dependencies in package.json

---

## 📚 RESOURCES

- Next.js: https://nextjs.org/docs
- Tailwind: https://tailwindcss.com/docs
- Recharts: https://recharts.org
- Vercel: https://vercel.com/docs

---

## 📝 LICENSE

Created for Atelier 8 - Luxury Restoration Studio
Based on PBL Report by Kanav Garg

---

## ✨ READY TO DEPLOY!

Your complete dashboard is ready. Follow the Quick Start guide above.

**Need help?** Check the files in the project - they're well-commented.
