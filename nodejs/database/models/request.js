'use strict';

module.exports = (sequelize, DataTypes) => {
    const request = sequelize.define('request', {
        id_request: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        status: {
            type: DataTypes.ENUM(['Donation', 'Processing', 'Testing', 'Distribution']),
        },
        blood_type: {
            type: DataTypes.STRING(5),
        },
        Rh: {
            type: DataTypes.ENUM(['Positive', 'Negative']),
        },
        receiving_person: {
            type: DataTypes.STRING(60),
            allowNull: true
        },
        quantity: {
            type: DataTypes.FLOAT,
            allowNull: true
        },
        id_doctor: {
            type: DataTypes.INTEGER
        },
        id_center: {
            type: DataTypes.INTEGER
        }
    }, {
        freezeTableName: true,
        timestamps: false,
        underscored: true,
        name: {
            singular: 'request',
            plural: 'request'
        }
    });

    request.associate = models => {
        request.belongsTo(models.doctor, {
            foreignKey: 'id_doctor'
        });

        request.belongsTo(models.transfusion_center, {
            foreignKey: 'id_center'
        });

        request.hasMany(models.donation, {
            foreignKey: 'id_request',
            onDelete: 'cascade'
        })
    };

    return request;
};
