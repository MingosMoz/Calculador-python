# mean_var_std.py

import numpy as np

def calculate(numbers):
    """
    Calcula a média, variância, desvio-padrão, máximo, mínimo e soma das linhas, colunas e elementos em uma matriz de 3x3.

    Args:
        numbers (list): Uma lista com 9 algarismos.

    Returns:
        dict: Um dicionário contendo os resultados.
    """
    if len(numbers) != 9:
        raise ValueError("A lista deve conter nove números.")

    # Converte a lista em uma matriz 3x3 do NumPy
    matrix = np.array(numbers).reshape(3, 3)

    # Calcula os resultados
    results = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    }

    return results