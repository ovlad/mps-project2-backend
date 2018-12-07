'use strict';

module.exports = {
    development: {
        'dialect': 'mysql',
        'host': 'mps2db.mysql.database.azure.com',
        'username': process.env.MYSQL_USERNAME,
        'password': process.env.MYSQL_PASSWORD,
        'database': 'mps2projectdev1',
        "ssl": true,
        "dialectOptions": {
            "ssl": {}
        },
        'operatorsAliases': false,
        'seederStorage': 'sequelize',
        'migrationStorage': 'sequelize',
        'seederStorageTableName': '_SEQUELIZE_DATA',
        'migrationStorageTableName': '_SEQUELIZE_META',
        'pool': {
            'max': 15,
            'min': 0,
            'acquire': 30000,
            'idle': 10000
        },
    },
    production: {
        'dialect': 'mysql',
        'host': 'mps2db.mysql.database.azure.com',
        'username': process.env.MYSQL_USERNAME,
        'password': process.env.MYSQL_PASSWORD,
        'database': 'mps2project',
        "ssl": true,
        "dialectOptions": {
            "ssl": {}
        },
        'operatorsAliases': false,
        'seederStorage': 'sequelize',
        'migrationStorage': 'sequelize',
        'seederStorageTableName': '_SEQUELIZE_DATA',
        'migrationStorageTableName': '_SEQUELIZE_META',
        'logging': console.log,
        'pool': {
            'max': 15,
            'min': 0,
            'acquire': 30000,
            'idle': 10000
        },
    }
};
