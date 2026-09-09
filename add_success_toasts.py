import re

# 1. Update RemittanceMonitoringPage
with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    """    try {
      await verifyRemittance(id);
      fetchRemittances();
    } catch {""",
    """    try {
      await verifyRemittance(id);
      toast.success("Remittance verified successfully");
      fetchRemittances();
    } catch {"""
)

content = content.replace(
    """    try {
      await createRemittance({
        ...form,
        fuelTransaction: fuelTransaction?._id,
      });
      setShowForm(false);
      fetchRemittances();
    } catch {""",
    """    try {
      await createRemittance({
        ...form,
        fuelTransaction: fuelTransaction?._id,
      });
      toast.success("Remittance logged successfully");
      setShowForm(false);
      fetchRemittances();
    } catch {"""
)

with open('frontend/src/pages/admin/RemittanceMonitoringPage.jsx', 'w') as f:
    f.write(content)

# 2. Update MaintenanceDashboard
with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'r') as f:
    content = f.read()

content = content.replace(
    """    try {
      await updateMaintenance(
        editingMaintenance._id,
        formData
      );
      setEditingMaintenance(null);
      setRefreshing((r) => !r);
    } catch (err) {""",
    """    try {
      await updateMaintenance(
        editingMaintenance._id,
        formData
      );
      toast.success("Maintenance updated successfully");
      setEditingMaintenance(null);
      setRefreshing((r) => !r);
    } catch (err) {"""
)

content = content.replace(
    """    try {
      await createMaintenance(formData);
      setOpenCreateModal(false);
      setRefreshing((r) => !r);
    } catch (err) {""",
    """    try {
      await createMaintenance(formData);
      toast.success("Maintenance ticket created successfully");
      setOpenCreateModal(false);
      setRefreshing((r) => !r);
    } catch (err) {"""
)

content = content.replace(
    """    try {
      await assignMechanic(
        maintenanceId,
        mechanicId
      );
      setRefreshing((r) => !r);
    } catch (err) {""",
    """    try {
      await assignMechanic(
        maintenanceId,
        mechanicId
      );
      toast.success("Mechanic assigned successfully");
      setRefreshing((r) => !r);
    } catch (err) {"""
)

content = content.replace(
    """    try {
      await updateMaintenanceStatus(
        maintenanceId,
        newStatus
      );
      setRefreshing((r) => !r);
    } catch (err) {""",
    """    try {
      await updateMaintenanceStatus(
        maintenanceId,
        newStatus
      );
      toast.success(`Maintenance status updated to ${newStatus}`);
      setRefreshing((r) => !r);
    } catch (err) {"""
)

with open('frontend/src/pages/admin/MaintenanceDashboard.jsx', 'w') as f:
    f.write(content)

