fn generate_expected_combinations(s: &str, k: usize) -> Vec<String> {
    let chars: Vec<char> = s.chars().collect();
    let n = chars.len();
    let mut result = Vec::new();

    if k > n {
        return result;
    }
    if k == 0 {
        return vec![String::new()];
    }

    // Enumerate all 2^n subsets and filter by popcount == k
    for mask in 0..(1usize << n) {
        if mask.count_ones() as usize == k {
            let mut combo = String::new();
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    combo.push(chars[i]);
                }
            }
            result.push(combo);
        }
    }
    result.sort();
    result
}

fn main() {
    let s1 = "abcd".to_string();
    let k1 = 3;
    let s2 = String::new();
    let k2 = 2;
    let s3 = "rat".to_string();
    let k3 = 3;
    let s4 = "rat".to_string();
    let k4 = 1;
    let s5 = "rat".to_string();
    let k5 = 0;
    let s6 = "abcdefghijklmnopqrstuvwxyz".to_string();
    let k6 = 1;
    let s7 = s6.clone();
    let k7 = 5;
    let s8 = "abcd".to_string();
    let k8 = 5;

    let test_cases: Vec<((String, usize), Vec<String>)> = vec![
        ((s1.clone(), k1), generate_expected_combinations(&s1, k1)),
        ((s2.clone(), k2), generate_expected_combinations(&s2, k2)),
        ((s3.clone(), k3), generate_expected_combinations(&s3, k3)),
        ((s4.clone(), k4), generate_expected_combinations(&s4, k4)),
        ((s5.clone(), k5), generate_expected_combinations(&s5, k5)),
        ((s6.clone(), k6), generate_expected_combinations(&s6, k6)),
        ((s7.clone(), k7), generate_expected_combinations(&s7, k7)),
        ((s8.clone(), k8), generate_expected_combinations(&s8, k8)),
    ];

    std::process::exit(run_tests!(&test_cases, |input| combs(&input.0, input.1)));
}
