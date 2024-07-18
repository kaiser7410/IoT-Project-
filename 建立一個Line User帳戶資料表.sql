USE [IoTDB]
GO

/****** Object:  Table [dbo].[LineUser]    Script Date: 2023/12/26 �U�� 02:39:57 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[LineUser](
	[UserId] [varchar](50) NOT NULL,
	[Name] [nvarchar](50) NOT NULL,
	[PictureURL] [varchar](50) NULL,
	[Active] [bit] NULL,
	[CreateDate] [datetime] NULL,
	[ModiDate] [date] NULL,
 CONSTRAINT [PK_LineUser] PRIMARY KEY CLUSTERED 
(
	[UserId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[LineUser] ADD  CONSTRAINT [DF_LineUser_Active]  DEFAULT ((1)) FOR [Active]
GO

ALTER TABLE [dbo].[LineUser] ADD  CONSTRAINT [DF_LineUser_CreateDate]  DEFAULT (getdate()) FOR [CreateDate]
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Line User ID �t�νs �㦳�ߤ@��' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'LineUser', @level2type=N'COLUMN',@level2name=N'UserId'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�ϥΪ̵��U�e�{�W��' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'LineUser', @level2type=N'COLUMN',@level2name=N'Name'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�Ϲ� ������}' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'LineUser', @level2type=N'COLUMN',@level2name=N'PictureURL'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'���ĩ�  1-�Ұ� 0-����F' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'LineUser', @level2type=N'COLUMN',@level2name=N'Active'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N' �[�J���' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'LineUser', @level2type=N'COLUMN',@level2name=N'CreateDate'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�̫����Ϊ̫��� ���' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'LineUser', @level2type=N'COLUMN',@level2name=N'ModiDate'
GO


