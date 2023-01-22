import hashlib

hash_algorithms = ['md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'sha3_512']
file_path = 'SkillFront-SFE016b2e274f651-39098380485039.pdf'

with open(file_path, 'rb') as afile:
    buf = afile.read()
    for algorithm in hash_algorithms:
        hasher = getattr(hashlib, algorithm)()
        hasher.update(buf)
        print(f'{algorithm.upper()} Hash String: {hasher.hexdigest()}')






