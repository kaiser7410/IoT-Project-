--�إ߷P������ƪ�SensorData
USE [IoTDB]
GO
CREATE TABLE [dbo].[SensorData](
	[SensorID] [char](6) NOT NULL,
	[Description] [nvarchar](50) NOT NULL,
	[Type] [nvarchar](50) NOT NULL,
	[SetupDate] [date] NULL,
	[Location] [nvarchar](40) NULL,
	[CreateDate] [date] NULL,
 CONSTRAINT [PK_SensorData_1] PRIMARY KEY CLUSTERED 
(
	[SensorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[SensorData] ADD  CONSTRAINT [DF_SensorData_CreateDate]  DEFAULT (getdate()) FOR [CreateDate]
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�P�����s��_�PCHT IOT�s���A�㦳�ߤ@��' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'SensorData', @level2type=N'COLUMN',@level2name=N'SensorID'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�Բӻ���' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'SensorData', @level2type=N'COLUMN',@level2name=N'Description'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�]�ƭ�l����' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'SensorData', @level2type=N'COLUMN',@level2name=N'Type'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�w�ˤ��(NULL �|���w��-�w�s)' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'SensorData', @level2type=N'COLUMN',@level2name=N'SetupDate'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�w�˦a�I(NULL �|���w��)' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'SensorData', @level2type=N'COLUMN',@level2name=N'Location'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�ʤJ���' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'SensorData', @level2type=N'COLUMN',@level2name=N'CreateDate'
GO


