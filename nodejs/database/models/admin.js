'use strict';

module.exports = (sequelize, DataTypes) => {
    return sequelize.define('admin', {
        id_admin: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING(30),
        },
        surname: {
            type: DataTypes.STRING(30),
        },
        mail: {
            type: DataTypes.STRING(30),
        },
        password: {
            type: DataTypes.STRING(30),
        }
    }, {
        freezeTableName: true,
        timestamps: false,
        underscored: true,
        name: {
            singular: 'admin',
            plural: 'admin'
        }
    });
};
