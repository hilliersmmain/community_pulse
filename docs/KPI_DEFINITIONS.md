# Key Performance Indicator (KPI) Definitions

## Overview

This document defines the key metrics used in the Community Pulse Analytics Dashboard to measure member engagement and data quality. Each KPI includes its calculation method, interpretation guidelines, and target benchmarks.

---

## Member Engagement Metrics

These metrics help assess how actively members participate in the organization and track growth patterns.

### 1. Member Growth Rate

**Definition**: The percentage change in total member count over a specified time period (typically monthly).

**Formula**:

```
Growth Rate = ((Current Month Members - Previous Month Members) / Previous Month Members) × 100
```

**Interpretation**:

- **Positive value**: Member base is growing
- **Negative value**: Member attrition exceeds new sign-ups
- **Zero**: Stable membership

**Target Benchmark**: +5% monthly growth

**Data Source**: Derived from `Join_Date` field by counting unique members joining in each month

---

### 2. Average Event Attendance

**Definition**: The mean number of events attended per member across the entire member base.

**Formula**:

```
Avg Attendance = Sum of all Event_Attendance values / Total number of members
```

**Interpretation**:

- **Higher values (>10)**: Highly engaged member base
- **Mid-range (5-10)**: Moderate engagement
- **Lower values (<5)**: Opportunity to increase event participation

**Target Benchmark**: 8+ events per member annually

**Data Source**: Calculated from the `Event_Attendance` column

**Usage**: Helps identify if engagement initiatives are working and whether events are reaching the community

---

### 3. Engagement Score

**Definition**: A composite metric combining attendance frequency with recency of last login to assess overall member activity.

**Formula**:

```
Engagement Score = (Event_Attendance × 0.7) + (Days Since Last Login × 0.3)
```

_Note: Days since login is normalized to a 0-100 scale where recent logins score higher_

**Interpretation**:

- **High (>70)**: "Super Users" - highly active members
- **Medium (40-69)**: Regular members with moderate activity
- **Low (<40)**: At-risk members who may need re-engagement

**Target Benchmark**: 60% of members should score >50

**Data Source**: Combines `Event_Attendance` and `Last_Login` fields

**Usage**: Prioritize re-engagement campaigns for low-scoring members

---

## Data Health Metrics

These metrics measure the quality and cleanliness of the member data in the CRM system.

### 4. Duplicate Rate

**Definition**: The percentage of records that are duplicates based on email address matching.

**Formula**:

```
Duplicate Rate = (Number of Duplicate Records / Total Raw Records) × 100
```

**Interpretation**:

- **Healthy (<5%)**: Well-maintained data entry processes
- **Concerning (5-10%)**: Review data entry procedures
- **Critical (>10%)**: Immediate process improvement needed

**Target Benchmark**: <5%

**Data Source**: Detected during the cleaning pipeline's deduplication step

**Usage**: Monitors CRM data entry quality; high rates indicate need for staff training or validation rules

---

### 5. Missing Data Rate

**Definition**: The percentage of records with null or missing values in critical fields.

**Formula**:

```
Missing Data Rate = (Total Missing Values Across Key Fields / (Total Records × Number of Key Fields)) × 100
```

**Key Fields Tracked**: Email, Event_Attendance, Join_Date, Last_Login

**Interpretation**:

- **Excellent (<2%)**: Complete and reliable data
- **Acceptable (2-5%)**: Minor gaps, manageable
- **Poor (>5%)**: Insights may be skewed by incomplete data

**Target Benchmark**: <3%

**Data Source**: Calculated from null/NaN counts before cleaning

**Usage**: Identifies data collection gaps; helps prioritize which fields need mandatory entry rules

---

### 6. Email Validity Rate

**Definition**: The percentage of email addresses that pass basic format validation (contains "@" and a domain).

**Formula**:

```
Email Validity Rate = (Valid Emails After Cleaning / Total Emails Before Cleaning) × 100
```

**Interpretation**:

- **Excellent (>95%)**: Clean CRM data
- **Good (90-95%)**: Some legacy data issues
- **Poor (<90%)**: Systemic data quality problems

**Target Benchmark**: >95%

**Data Source**: Tracked during the email cleaning step

**Usage**: Directly impacts email campaign deliverability; low rates suggest need for email verification tools

---

## Role Distribution Metric

### 7. Member Type Breakdown

**Definition**: The percentage distribution of members across different role categories.

**Calculation**:

```
Role % = (Count of Members in Role / Total Members) × 100
```

**Standard Roles**:

- **Member**: Regular community participants (target: ~80%)
- **Admin**: Leadership and staff (target: ~5%)
- **Guest**: Trial or limited-access users (target: ~15%)

**Interpretation**: Helps understand community composition and whether the organization maintains a healthy ratio of engaged members to administrative oversight.

**Data Source**: `Role` column

---

## Dashboard Usage Notes

- All metrics are calculated **after** data cleaning to ensure accuracy
- Time-series metrics (e.g., Growth Rate) require at least 2 months of data
- Use the **Role Filter** in the Analytics Dashboard to segment metrics by member type
- KPIs refresh automatically when you re-run the cleaning pipeline with updated data

---

## Reporting Frequency

| Metric                   | Recommended Review Frequency      |
| ------------------------ | --------------------------------- |
| Member Growth Rate       | Monthly                           |
| Average Event Attendance | Quarterly                         |
| Engagement Score         | Monthly (for targeting campaigns) |
| Duplicate Rate           | Weekly                            |
| Missing Data Rate        | Monthly                           |
| Email Validity Rate      | Monthly                           |

---

## Document Control

- **Version**: 1.0
- **Last Updated**: December 2025
- **Owner**: Analytics Team
- **Review Cycle**: Bi-annually
