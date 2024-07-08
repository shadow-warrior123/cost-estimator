def get_user_inputs():
    grade = input("Enter the grade of concrete (e.g., 'M20'): ")
    concrete_type = input("Enter the type of concrete (PCC for Plain, RCC for Reinforced): ")
    exposure_condition = input("Enter the exposure condition (e.g., 'Mild', 'Moderate', etc.): ")
    cement_type = input("Enter the type of cement (e.g., 'OPC 33', 'OPC 43', 'OPC 53', 'PPC', 'PSC'): ")
    coarse_aggregate_size = int(input("Enter the size of the coarse aggregate (10, 20, 30 mm): "))
    target_slump = int(input("Enter the target slump value (in mm): "))
    admixture_used = input("Is an admixture used? (yes/no): ").strip().lower() == 'yes'
    fine_aggregate_zone = input("Enter the zone of the fine aggregate (Zone I, Zone II, Zone III, Zone IV): ")
    pump_required = input("Is concrete pumping required? (yes/no): ").strip().lower() == 'yes'
    return grade, concrete_type, exposure_condition, cement_type, coarse_aggregate_size, target_slump, admixture_used, fine_aggregate_zone, pump_required
