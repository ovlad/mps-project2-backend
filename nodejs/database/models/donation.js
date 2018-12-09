'use strict';

module.exports = (sequelize, DataTypes) => {
    const donation = sequelize.define('donation', {
        id_donation: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        bloodTest: {
            type: DataTypes.BLOB,
            allowNull: true
        },
        date: {
            type: DataTypes.DATE,
        },
        quantity: {
            type: DataTypes.FLOAT,
            allowNull: true
        },
        id_donor: {
            type: DataTypes.INTEGER
        },
        id_request: {
            type: DataTypes.INTEGER
        }
    }, {
        freezeTableName: true,
        timestamps: false,
        underscored: true,
        name: {
            singular: 'donation',
            plural: 'donation'
        }
    });

    donation.associate = models => {
        donation.belongsTo(models.donor, {
            foreignKey: 'id_donor'
        });

        donation.belongsTo(models.request, {
            foreignKey: 'id_request'
        });
    };

    return donation;
};
