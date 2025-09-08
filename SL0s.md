# Service Level Objectives (SLOs) — Kata Dictionary

This document defines the reliability targets and error budgets 
for the kata-dictionary service.

---

## 🔹 Service Level Indicators (SLIs)

- **Availability**: Percentage of successful lookups (hits vs total requests).  
- **Latency**: Time taken to respond to a lookup request.  
- **Error Rate**: Ratio of failed lookups (misses) to total lookups.  

---

## 🔹 Service Level Objectives (SLOs)

- **Availability SLO**: 99% of lookup requests should succeed.  
- **Latency SLO**: 95% of lookups must return in <200ms.  
- **Error Rate SLO**: Lookup miss ratio should remain below 5% over 30 days.  

---

## 🔹 Error Budget

- Allowed downtime = 1% per month (~7.2 hours).  
- Allowed error budget = 5% of requests failing per month.  

If the error budget is exceeded:  
- Feature rollouts pause.  
- Focus shifts to reliability improvements (fixes, scaling, tuning).  

---

## 🔹 Monitoring & Alerts

- **Prometheus** metrics from `dictionary_requests_total`.  
- **PrometheusRule** → alerts when error ratio >20% for 5 minutes.  
- Grafana dashboard for visualization.  
