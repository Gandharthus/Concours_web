UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'csv'}
CHOICE_CODES={6108:'casa', 7102:'meknes', 5660:'rabat'}
ENSAM_CODES=dict((v, k) for k, v in CHOICE_CODES.items())
SECRET_KEY = '002a5938ad85bac7145ce707c8404ce0cf4a94c4ee705734'