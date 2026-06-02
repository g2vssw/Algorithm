import math

def solution(fees, records):
    answer = []
    value = {}
    records_dict = {}
    base_time, base_fee, unit_time, unit_fee = fees
    
    for record in records:
        record_list = record.split()
        if record_list[2] == "IN":
            records_dict[record_list[1]] = record_list[0]
        else:
            in_h, in_m = map(int, records_dict[record_list[1]].split(":"))
            out_h, out_m = map(int, record_list[0].split(":"))
            in_t = in_h * 60 + in_m
            out_t = out_h * 60 + out_m
            t = out_t - in_t
            value[record_list[1]] = value.get(record_list[1], 0) + t
            del records_dict[record_list[1]]
    
    for record in records_dict:
        in_h, in_m = map(int, records_dict[record].split(":"))
        in_t = in_h * 60 + in_m
        t = 23 * 60 + 59 - in_t
        value[record] = value.get(record, 0) + t
        
    value_key_list = sorted(list(value.keys()))
    
    for key in value_key_list:
        value_time = value[key]
        if value_time > base_time:
            result = base_fee + math.ceil((value_time - base_time) / unit_time) * unit_fee
        else:
            result = base_fee
        answer.append(result)
        
    return answer