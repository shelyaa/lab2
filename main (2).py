import numpy as np
from scipy.stats import t

sample_sizes = [50, 115, 200]
samples = {
    50: [3, 5, 5, 1, 11, 4, 3, 4, 5, 6, 5, 4, 7, 5, 3, 3, 7, 3, 5, 5, 3, 6, 4, 7, 4, 6, 6, 9, 4, 5, 7, 6, 6, 4, 7, 9, 4, 5, 3, 1, 4, 6, 4, 3, 6, 5, 6, 3, 4, 4],
    115: [4, 8, 5, 7, 4, 4, 4, 6, 8, 4, 5, 1, 7, 3, 6, 2, 5, 6, 5, 6, 2, 4, 5, 2, 6, 7, 6, 5, 3, 7, 6, 4, 7, 2, 6, 4, 4, 6, 8, 4, 3, 3, 5, 8, 4, 7, 5, 7, 5, 3, 8, 7, 5, 7, 4, 5, 7, 3, 4, 2, 6, 4, 3, 4, 7, 6, 7, 5, 5, 2, 5, 2, 5, 4, 7, 6, 0, 7, 2, 7, 4, 6, 8, 4, 10, 6, 6, 4, 5, 4, 2, 4, 7, 3, 4, 4, 3, 8, 4, 5, 7, 8, 6, 8, 3, 6, 5, 7, 6, 7, 5, 4, 3, 4, 2],
    200: [5, 3, 3, 6, 4, 7, 5, 6, 5, 5, 3, 3, 8, 5, 5, 4, 10, 4, 2, 8, 6, 4, 4, 8, 5, 4, 5, 7, 5, 9, 6, 8, 2, 6, 9, 6, 2, 4, 9, 7, 4, 3, 6, 6, 5, 7, 6, 6, 5, 5, 5, 4, 7, 5, 6, 3, 4, 5, 4, 6, 4, 5, 5, 6, 5, 8, 5, 3, 4, 5, 8, 8, 6, 7, 3, 5, 4, 9, 7, 6, 6, 6, 4, 8, 7, 4, 5, 6, 3, 4, 8, 5, 5, 5, 9, 5, 4, 5, 6, 5, 7, 6, 6, 5, 4, 5, 4, 9, 2, 5, 7, 3, 6, 4, 6, 5, 6, 9, 5, 7, 6, 3, 5, 3, 4, 7, 7, 4, 10, 6, 4, 4, 4, 6, 5, 10, 3, 6, 7, 7, 2, 2, 4, 4, 8, 2, 5, 5, 8, 8, 4, 8, 1, 4, 6, 5, 9, 7, 4, 6, 4, 9, 6, 5, 5, 5, 9, 5, 8, 1, 3, 5, 6, 3, 6, 6, 8, 6, 5, 4, 7, 6, 4, 6, 6, 6, 5, 4, 4, 3, 4, 5, 6, 6, 4, 7, 6, 5, 7, 3]
}
conf_level = 0.95
est_mean = []
est_std = []
conf_ints_mean = []
conf_ints_std = []

for sample_size in sample_sizes:
    sample = samples[sample_size]

    mean_est = np.mean(sample)
    est_mean.append(mean_est)

    std_est = np.std(sample, ddof=1)
    est_std.append(std_est)

    #Довірчий інтервал для математичного сподівання
    st_error_mean = std_est / np.sqrt(sample_size)
    mar_error_mean = st_error_mean * t.ppf((1 + conf_level) / 2, sample_size - 1)
    conf_int_mean = (mean_est - mar_error_mean, mean_est + mar_error_mean)
    conf_ints_mean.append(conf_int_mean)

    #Довірчий інтервал для середньоквадратичного відхилення
    df = sample_size - 1
    st_error_std = std_est / np.sqrt(2 * df)
    mar_error_std = st_error_std * t.ppf((1 + conf_level) / 2, df)
    conf_int_std = (std_est - mar_error_std, std_est + mar_error_std)
    conf_ints_std.append(conf_int_std)

#Вивід результатів
for i in range(len(sample_sizes)):
    print(f"Розмір вибірки: {sample_sizes[i]}")
    print(f"Оцінка математичного сподівання: {est_mean[i]}")
    print(f"Довірчий інтервал для математичного сподівання: {conf_ints_mean[i]}")
    print(f"Оцінка средньоквадратичного відхилення: {est_std[i]}")
    print(f"Довірчий інтервал для средньоквадратичного відхилення: {conf_ints_std[i]}\n")