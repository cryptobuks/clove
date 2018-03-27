COLORED_LOGS_STYLES = {
    'info': {'color': 'green'},
    'error': {'color': 'red'},
    'debug': {'color': 'magenta'},
    'warning': {'color': 'yellow'}
}
NODE_COMMUNICATION_TIMEOUT = 2 * 60
TRANSACTION_BROADCASTING_MAX_ATTEMPTS = 10

SIGNATURE_SIZE = 110

BLOCKCYPHER_SUPPORTED_NETWORKS = (
    'btc', 'ltc', 'doge', 'dash'
)

CRYPTOID_SUPPORTED_NETWORKS = (
    '1337', '2give', '42', '8bit', 'abc', 'ac', 'adc', 'aeg', 'anc', 'arco',
    'arg', 'atms', 'atom', 'b3', 'bash', 'bay', 'bcc', 'bee2', 'bela', 'bitb',
    'blitz', 'blk', 'block', 'boli', 'brit', 'bro', 'bsd', 'bta', 'btc', 'btci',
    'btd', 'btdx', 'btg', 'btm', 'btx', 'bucks', 'bxt', 'byc', 'byz', 'bzl',
    'cach', 'cann', 'c2', 'carbon', 'cbx', 'ccc', 'ccn', 'chao', 'chbt', 'civ',
    'club', 'cnc', 'cno', 'colx', 'corg', 'cpc', 'cqst', 'crea', 'crypt',
    'crw', 'cure', 'dash', 'dgb', 'dgc', 'dime', 'dmd', 'dmx', 'dnr', 'dollar',
    'dope', 'dot', 'drs', 'drz', 'dtc', 'dvc', 'eac', 'ebc', 'ec', 'ecc',
    'ecn', 'efl', 'egc', 'egcc', 'emc2', 'emd', 'enrg', 'ent', 'eqt', 'erc',
    'ery', 'fail', 'flax', 'fuel', 'funk', 'gam', 'gap', 'gcr', 'geo', 'glc',
    'gld', 'gre', 'grn', 'grs', 'grs-test', 'gun', 'hbn', 'hxx', 'i0c', 'icn',
    'imx', 'info', 'infx', 'insn', 'ioc', 'ion', 'itc', 'ivc', 'ixc', 'j',
    'karm', 'klk', 'knc', 'kobo', 'kore', 'koruna', 'kush', 'lana', 'lems',
    'lir', 'lol', 'loc', 'ltc', 'lux', 'linx', 'ltca', 'mac', 'manna', 'max',
    'maxt', 'may', 'mbch', 'mec', 'meow', 'mnd', 'mojo3', 'moon', 'mscn',
    'mst', 'mue', 'nav', 'ned', 'neos', 'netko', 'neva', 'nobl', 'note', 'npc',
    'nro', 'nxx', 'oc', 'octo', 'off', 'ok', 'opal', 'ozc', 'pak', 'part',
    'pho', 'phr', 'piggy', 'pink', 'pivx', 'pnd', 'poker', 'post', 'pot',
    'ppc', 'ppc-test', 'pr', 'psb', 'ptc', 'pura', 'put', 'pxi', 'pwc', 'qrk',
    'rads', 'rads-test', 'rbc', 'rby', 'ric', 'rns', 'rsgp', 'scol', 'sfr',
    'sh', 'sha', 'skc', 'slg', 'slr', 'smly', 'snrg', 'spr', 'sprts', 'spz',
    'src', 'stk', 'strat', 'strat-test', 'stv', 'super', 'sync', 'swift',
    'swing', 'sxc', 'sys', 'szc', 'taj', 'talk', 'tech', 'tes', 'toa', 'tpwr',
    'troll', 'trump', 'trust', 'tx', 'tzc', 'ubiq', 'ufo', 'uni', 'uno', 'usc',
    'vash', 'vgs', 'via', 'visio', 'vivo', 'vlx', 'vrc', 'vrm', 'vtc', 'vuc',
    'wac', 'wbc', 'wc', 'wc-old', 'wex', 'worm', 'wsx', 'wyv', 'ww', 'x2c',
    'xc', 'xcs', 'xjo', 'xlr', 'xmg', 'xmy', 'xp', 'xpy', 'xqn', 'xspec',
    'xst', 'xstc', 'xto', 'xvp', 'xzc', 'zeit', 'zet', 'zoi'
)

NETWORKS_WITH_API = BLOCKCYPHER_SUPPORTED_NETWORKS + CRYPTOID_SUPPORTED_NETWORKS

ETH_REDEEM_GAS_LIMIT = 100000
