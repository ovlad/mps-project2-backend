'use strict';

module.exports = (sequelize, DataTypes) => {
    const donor = sequelize.define('donor', {
        id_donor: {
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
        },
        blood_type: {
            type: DataTypes.STRING(5),
        },
        Rh: {
            type: DataTypes.ENUM(['Positive', 'Negative']),
        },
    }, {
        freezeTableName: true,
        timestamps: false,
        underscored: true,
        name: {
            singular: 'donor',
            plural: 'donor'
        }
    });

    donor.associate = models => {
        donor.hasMany(models.donation, {
            foreignKey: 'id_donor',
            onDelete: 'cascade'
        });
    };

    return donor;
};
