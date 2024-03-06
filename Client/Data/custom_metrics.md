# Custom Metrics

## Implementing Active Directory to Metrics

### Defining The Metric Namespace
```python
ADUsers = Metric("ADUsers", null)
```

### Implementation of Metric
```python
def get_custom_metrics():
  command = "powershell.exe Get-ADUser -Filter * -SearchBase 'DC=yourdomain,DC=com' | Measure-Object | Select-Object -ExpandProperty Count"
  result = subprocess.check_output(command, shell=True)
  user_count = int(result.decode().strip())

  ADUsers.value = user_count
```
