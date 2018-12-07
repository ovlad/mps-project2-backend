'use strict';

module.exports = (sequelize, DataTypes) => {
    const hospital = sequelize.define('hospital', {
        id_hospital: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING(50),
            defaultValue: null
        }
    }, {
        freezeTableName: true,
        underscored: true,
        name: {
            singular: 'hospital',
            plural: 'hospital'
        }
    });

    hospital.associate = models => {
        hospital.hasMany(models.doctor, {
            foreignKey: 'id_hospital',
            onDelete: 'cascade'
        });
    };

    return hospital;
};
