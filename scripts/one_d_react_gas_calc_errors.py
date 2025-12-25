#!/usr/bin/python

def load_data(filename):
    x_vals, y_vals = [], []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if not line.strip() or line.strip().startswith('#'):
                    continue
                parts = line.replace(',', ' ').split()
                if len(parts) >= 2:
                    x_vals.append(float(parts[0]))
                    y_vals.append(float(parts[1]))
    except FileNotFoundError:
        return None, None
    return x_vals, y_vals

def calculate_normalized_trapezoidal():
    x_ref, y_ref = load_data('ref.txt')
    x_num, y_num = load_data('num.txt')

    if not x_ref or not x_num:
        print("Error: Could not load data.")
        return

    num_len = len(x_num)
    last_idx = 0
    
    # Lists to store interpolated errors and ref values at x_ref points
    errors = []
    
    for i in range(len(x_ref)):
        tx = x_ref[i]
        
        # Optimized index tracking for interpolation
        while last_idx < num_len - 2 and x_num[last_idx + 1] < tx:
            last_idx += 1
            
        x1, x2 = x_num[last_idx], x_num[last_idx + 1]
        y1, y2 = y_num[last_idx], y_num[last_idx + 1]
        
        # Interpolation of y_num onto x_ref
        if tx <= x1:
            iy = y1
        elif tx >= x2 and last_idx == num_len - 2:
            iy = y2
        else:
            iy = y1 + (tx - x1) * (y2 - y1) / (x2 - x1)
            
        errors.append(abs(y_ref[i] - iy))

    # Trapezoidal Integration
    l1_integral = 0.0
    ref_integral = 0.0
    
    for i in range(len(x_ref) - 1):
        dx = x_ref[i+1] - x_ref[i]
        # L1 Integral: Area under the absolute error curve
        l1_integral += (errors[i] + errors[i+1]) * 0.5 * dx
        # Ref Integral: Area under the reference curve
        ref_integral += (abs(y_ref[i]) + abs(y_ref[i+1])) * 0.5 * dx

    # Final Normalization
    if ref_integral == 0:
        print("Error: Integral of y_ref is zero. Cannot normalize.")
        return

    normalized_l1 = l1_integral / ref_integral

    #print(f"L1 Integral Error: {l1_integral:.8e}")
    #print(f"Reference Integral: {ref_integral:.8e}")
    #print(f"Normalized L1 (L1_int / Ref_int): {normalized_l1:.8e}")
    print(f"{normalized_l1:.8f}")

if __name__ == "__main__":
    calculate_normalized_trapezoidal()
